import os, asyncio
from agents import Agent, Runner
from agents.mcp import MCPServerStdio
from config import DEFAULT_MODEL, API_KEY, API_BASE_URL
from pathlib import Path

# 💡 USB版 or PC版 の自動判定（手動で切り替えも可）
def is_usb_mode() -> bool:
    return os.path.exists("python-3.13.3-embed-amd64/python.exe")

# ① モード確認
USE_EMBED = is_usb_mode()


# 💻 分岐：コマンドと引数の準備
def get_command_and_args() -> tuple[str, list[str]]:
    if is_usb_mode():
        base = Path(__file__).resolve().parent
        python_path = str(base / "python-3.13.3-embed-amd64" / "python.exe")
        return python_path, ["-m", "mcp_proxy", "http://localhost:8000/sse"]
    else:
        proxy_path = os.path.join(os.environ["USERPROFILE"], ".local", "bin", "mcp-proxy.exe")
        return proxy_path, ["http://localhost:8000/sse", "--sse-port", "9000"]

# ② コマンドと引数を取得
command, args = get_command_and_args()


# ③ MCP サーバー起動設定
browser_use_stdio = MCPServerStdio(
    name="browser-server",
    params={
        "command": command,
        "args": args,
        "env": {
            "API_KEY": API_KEY,
            "API_BASE_URL": API_BASE_URL,
        },
    },
)

# ② Agent 本体
browser_use_agent = Agent(
    name="Browser Use Agent",
    instructions="""
You can control a headless browser via the browser-use MCP server.
""",
    model=DEFAULT_MODEL,
    mcp_servers=[browser_use_stdio],
)

# ③ テスト実行
if __name__ == "__main__":
    async def test():
        async with browser_use_stdio:
            print(f"💡 現在のモデル: {browser_use_agent.model}")
            while True:
                prompt = input("📥 指示を入力してね（終了は 'exit'）> ")
                if prompt.lower() in {"exit", "quit"}:
                    break
                res = await Runner.run(browser_use_agent, input=prompt)
                print("🖥️ RESULT:", res.final_output)

    asyncio.run(test())
