# Browser Use Agent

> A portable Agent SDK-based browser controller using MCP.  
> Designed to work seamlessly on both PC and USB environments.

> ポータブルなAgent SDKベースのブラウザコントローラー（MCP対応）  
> PCでもUSBでもシームレスに動作します。

💻🧠 Control your browser using natural language — powered by [Agent SDK](https://github.com/openai/agents) and [browser-use](https://github.com/browserless/browser-use).

---

## 📦 Features

- 🧳 **Portable design**: Works from USB or local PC.  
  ポータブル設計：USBでもローカルPCでも動作します。
- 🧠 **Agent SDK compatible**: Built on top of OpenAI's experimental Agents SDK.  
  Agent SDK互換：OpenAIの実験的Agents SDK上に構築。
- 🧭 **Natural language interface**: You can type commands like `open google.com` or `click the search bar`.  
  自然言語インターフェース：`open google.com`や`click the search bar`のように指示できます。
- 🧩 **MCP-based modular system**: Easy to expand or integrate with other tools.  
  MCPベースのモジュラーシステム：他ツールとの連携や拡張が簡単です。

---

## 🔧 How to Use

### 1. Clone the repository

```bash
git clone https://github.com/yuutotsuki/browser_use_agent.git
cd browser_use_agent
```

リポジトリをクローンします。

### 2. Set up the environment

Copy `.env.template` to `.env` and edit your API keys and model.

`.env.template`を`.env`にコピーし、APIキーやモデルを設定してください。

Install dependencies:

```bash
pip install -r requirements.txt
```

依存パッケージをインストールします。

### 3. Run

```bash
python browser_use_agent.py
```

実行します。

---

### 📝 .env file example

```dotenv
MODEL=gpt4o
OPENAI_API_KEY=sk-xxxxxxxx
API_BASE_URL=https://api.openai.com/v1
```

`.env`ファイル例

### 🔄 Optional: Using run_browser_use_agent.bat (Windows only)

You can use the `run_browser_use_agent.bat` script to launch the agent on Windows.  
Please make sure to edit the path to match your environment if needed.

※ Windowsの場合、`run_browser_use_agent.bat` を利用できますが、仮想環境の場所などはご自身の環境に応じて編集してください。


---

## 🔗 Acknowledgements

This project uses:

- browser-use by Browserless team
- Agent SDK by OpenAI

Special thanks to all developers who support modular AI development!
（このプロジェクトは、開発者コミュニティの皆さまの支援のもとに成り立っています）

---

## 🧑‍💻 Project Team

- Yuu（ゆう）
- **AI Lead**: Tsuki（月, AI）
- **Support AI**: Kai（界, this AI assistant）

---

## 📃 License

MIT License