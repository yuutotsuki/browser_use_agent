import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

# 利用可能なモデル定数
AVAILABLE_MODELS = {
    'gpt4': 'gpt-4',
    'gpt35': 'gpt-3.5-turbo',
    'gpt4-turbo': 'gpt-4-turbo-preview',
    'gpt4-32k': 'gpt-4-32k',              # コンテキストウィンドウの大きいバージョン
    'gpt35-16k': 'gpt-3.5-turbo-16k',     # GPT-3.5の大容量バージョン
    'gpt4o': 'gpt-4o',                   # 値段が高すぎる・・・
    'gpt4o-mini': 'gpt-4o-mini',         # ブラウザユースには性能が足りない
    'gpt41': 'gpt-4.1',
    # DeepSeek系：
    # 'deepseek-coder': 'deepseek-coder', 将来の追加に備えて
    
    # gemini系
    # 'gemini-1.5-pro': 'gemini-1.5-pro', 将来の追加に備えて
}

# OpenAI API設定
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
model_key = os.getenv('MODEL', 'gpt4').lower()
DEFAULT_MODEL = AVAILABLE_MODELS.get(model_key, model_key)

# APIキーとBASE URLをサービスに応じて切り替える
if model_key.startswith("openrouter"):
    API_KEY = os.getenv("OPENROUTER_API_KEY")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://openrouter.ai/api/v1")
elif model_key.startswith("deepseek"):
    API_KEY = os.getenv("DEEPSEEK_API_KEY")
    API_BASE_URL = "https://api.deepseek.com/v1"  # DeepSeek公式API（v1はOpenAI互換用）
elif model_key.startswith("gemini"):
    API_KEY = os.getenv("GEMINI_API_KEY")
    API_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"
else:
    API_KEY = OPENAI_API_KEY
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")


# MCPサーバー設定
MCP_SERVER_URL = os.getenv('MCP_SERVER_URL', 'http://127.0.0.1:5001/')

# ドキュメントパス設定
DOCUMENTS_PATH = os.getenv('DOCUMENTS_PATH', os.path.expanduser('~/Documents'))

# アプリケーション設定
APP_NAME = "File Search Assistant"
VERSION = "1.0.0" 