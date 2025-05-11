# Expandable Agent Seed

**日本語の説明書は下にあります。**

---

# Expandable Agent Seed (English)

A highly extensible template project for building AI agents.

---

## 📄 Overview

Expandable Agent Seed is a starter project designed to help you easily create "extensible agents."  
It comes with the following features out of the box, and you can freely add or expand functionalities as you like:

- Natural language file search
- Access to recently used files
- Integration with MCP (Model Context Protocol) servers

---

## 🚀 Setup

1. Clone this repository

    ```bash
    git clone https://github.com/yuutotsuki/expandable_agent_seed.git
    cd expandable_agent_seed
    ```

2. Create a Python virtual environment and install dependencies

    ```bash
    python -m venv venv
    # Windows (PowerShell)
    .\venv\Scripts\Activate.ps1
    # Mac/Linux
    source venv/bin/activate

    pip install -r requirements.txt
    ```

3. Create a `.env` file

    ```bash
    # Windows (PowerShell)
    Copy-Item .env.template .env
    # Mac/Linux
    cp .env.template .env
    ```

---

## ⚙️ Configuration

- `config.py` loads environment variables from `.env` or your system environment.
- Normally, you do not need to edit `config.py` directly.
- Please configure your environment using the `.env` file.

### Required settings in `.env`

| Key             | Description                        |
|-----------------|------------------------------------|
| OPENAI_API_KEY  | Your OpenAI API key                |
| OPENAI_MODEL    | Model name to use (e.g. gpt-4o)    |
| MCP_SERVER_URL  | MCP server URL                     |
| DOCUMENTS_PATH  | Local path to search for documents |

---

## 🖥️ Usage

Start the agent:

```bash
python expandable_agent_seed.py
```

### Example commands

- File search: "Search for report 2024"
- Show recent files: "Show me the last 5 files I used"
- Enter a number from the search results, then type `open` to open the file

---

## 📚 How to Extend

Expandable Agent Seed is designed to be easily extensible. For example:

- Add your own tools in `tools/`
- Add new MCP clients in `clients/`
- Add shared logic or utilities in `core/`

You can freely customize it to create your own AI assistant!

For keyword search, you can use this ready-made MCP server:  
[tsuki_mcp_filesystem_server](https://github.com/yuutotsuki/tsuki_mcp_filesystem_server)


---

## 💖 Special Thanks

This project was created through collaboration between AI and a human developer.

---

# Expandable Agent Seed (日本語)

拡張性抜群のAIエージェント雛形プロジェクト

---

## 📄 概要

Expandable Agent Seed は、「拡張可能なエージェント」を簡単に作り始められるシード（種）プロジェクトです。  
まずは以下の機能を備えていますが、ここから自由に機能を追加・拡張できます。

- 自然言語でファイル検索
- 最近使ったファイルの呼び出し
- MCP（Model Context Protocol）サーバーとの連携

---

## 🚀 セットアップ手順

1. このリポジトリをクローン

    ```bash
    git clone https://github.com/yuutotsuki/expandable_agent_seed.git
    cd expandable_agent_seed
    ```

2. Python仮想環境を作成し、必要なパッケージをインストール

    ```bash
    python -m venv venv
    # Windows (PowerShell)
    .\venv\Scripts\Activate.ps1
    # Mac/Linux
    source venv/bin/activate

    pip install -r requirements.txt
    ```

3. `.env` ファイルを作成

    ```bash
    # Windows (PowerShell)
    Copy-Item .env.template .env
    # Mac/Linux
    cp .env.template .env
    ```

---

## ⚙️ 設定ファイルについて

- `config.py` は `.env` またはシステム環境変数を読み込むための設定ファイルです。
- 通常は `config.py` を直接編集する必要はありません。
- 必要な設定は `.env` を通じて行ってください。

### .envファイルに記載する内容

| キー             | 説明                        |
|------------------|-----------------------------|
| OPENAI_API_KEY   | OpenAIのAPIキー             |
| OPENAI_MODEL     | 使用するモデル名（例: gpt-4o）|
| MCP_SERVER_URL   | MCPサーバーのURL            |
| DOCUMENTS_PATH   | 検索対象とするローカルパス  |

---

## 🖥️ 使い方

起動コマンド：

```bash
python expandable_agent_seed.py
```

### 使用例

- ファイル検索：「Search for report 2024」
- 最近使ったファイル一覧：「Show me the last 5 files I used」
- 検索結果から番号を入力 → `open` と入力してファイルを開く

---

## 📚 拡張方法

Expandable Agent Seed は「拡張前提」で設計されています。  
例えば…

- `tools/` に独自ツールを追加
- `clients/` に新しいMCPクライアントを追加
- `core/` に共通ロジックやユーティリティを追加

自分だけのAIアシスタントに自由にカスタマイズできます！

## キーワード検索　実行例

1、キーワード検索用のサーバー立ち上げ
2、expandable_agent_seedの実行

こちらの作成済みMCPサーバーが利用可能です： 
[tsuki_mcp_filesystem_server](https://github.com/yuutotsuki/tsuki_mcp_filesystem_server)

使用例
任意の場所にMCPサーバー（tsuki_mcp_filesystem_serberMCP）をセットアップ
例："C:\Users\ユーザー名\mcp_provider_python"

※仮想仮想環境の場合の実行例
PS C:\Users\ユーザー名\mcp_provider_python> .venv\Scripts\activate　仮想環境の有効化
(.venv) PS C:\Users\ユーザー名\mcp_provider_python> python ファイル名.py　MCPサーバーの起動

## 最近使ったファイルの検索

初期設定ではtoolを使用しています（MCPサーバー不使用）
---

## 💖 Special Thanks

このプロジェクトは、AIと人間の共同作業で生まれました。

