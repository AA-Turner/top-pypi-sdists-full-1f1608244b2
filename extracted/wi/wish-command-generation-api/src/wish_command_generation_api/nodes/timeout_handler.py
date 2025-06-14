"""Timeout handler node for the command generation graph."""

import json
import logging
from typing import Annotated

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from wish_models.command_result import CommandInput
from wish_models.settings import Settings

from ..constants import DEFAULT_TIMEOUT_SEC, DIVIDE_AND_CONQUER_DOC, FAST_ALTERNATIVE_DOC
from ..models import GraphState

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle_timeout(state: Annotated[GraphState, "Current state"], settings_obj: Settings) -> GraphState:
    """Handle timeout errors by applying fast alternatives or divide-and-conquer strategies.

    Args:
        state: The current graph state.

    Returns:
        Updated graph state with modified commands.
    """
    try:
        # If no act_result or not a timeout error, return the original state
        if not state.act_result or state.error_type != "TIMEOUT":
            logger.info("No timeout error to handle")
            return state

        # Create the LLM
        model = settings_obj.OPENAI_MODEL or "gpt-4o"
        llm = ChatOpenAI(model=model, temperature=0.2)

        # Create the prompt
        prompt = ChatPromptTemplate.from_template(
            """あなたは合法なペネトレーションテストに従事しているAIです。

ペネトレーションテストのディレクターから以下を受け取ります。
- 実行すべき「タスク」の指示
- あなたが以前出力しTIMEOUTとなったコマンドについての「フィードバック」
- 今回のタスクに役立つ可能性が高い「参考ドキュメント」
- コマンド高速化のための「高速な代替コマンド案」
- コマンド並列化のための「分割統治案」

フィードバックのコマンド列を、次はタイムアウトを起こさないものに修正してください。

各コマンドは `bash -c "（あなたの出力）"` として実行されるため、複数のコマンドをパイプなどでつなげることもできます。
各コマンドは並列実行されます。「`./a` の後に `./b` を実行する必要がある」ようなデータ依存がある場合は、
パイプや `&&` を使って1個のコマンド文字列で表現してください。

実行ログはファイルではなく、標準出力と標準エラー出力にdumpしてください。

以下の手順で考えましょう。

1. 「タスク」を理解し、「参考ドキュメント」から関連情報を探します。
2. 「フィードバック」から、前に使用したコマンドを確認します。
3. 前に使用したコマンドに「高速な代替コマンド案」があれば、それを使ったコマンドを出力して終了してください。
4. さもなければ、前に使用したコマンドに「分割統治案」があれば、それを使ったコマンドを出力して終了してください。
5. さもなければ、タイムアウトを倍増し、前に使用したコマンドと同じコマンドを出力してください。

# タスク
{query}

# フィードバック
{feedback}

# 参考ドキュメント
{context}

# 高速な代替コマンド案
{fast_alternative_doc}

# 分割統治案
{divide_and_conquer_doc}

出力は以下の形式のJSONで返してください:
{{ "command_inputs": [
  {{
     "command": "コマンド1",
     "timeout_sec": タイムアウト秒数（数値）
  }},
  {{
     "command": "コマンド2",
     "timeout_sec": タイムアウト秒数（数値）
  }}
]}}

JSONのみを出力してください。説明や追加のテキストは含めないでください。
"""
        )

        # Format the feedback as JSON string
        feedback_str = (
            json.dumps([result.model_dump() for result in state.act_result], ensure_ascii=False)
            if state.act_result else "[]"
        )

        # Format the context
        context_str = ""
        if isinstance(state.context, dict) and "history" in state.context:
            context_str = "Command History:\n" + "\n".join(state.context["history"])
        elif isinstance(state.context, dict):
            context_str = json.dumps(state.context, ensure_ascii=False)
        else:
            context_str = "No context available"

        try:
            # Create the chain
            chain = prompt | llm | StrOutputParser()

            # Invoke the chain
            result = chain.invoke({
                "query": state.query,
                "feedback": feedback_str,
                "context": context_str,
                "fast_alternative_doc": FAST_ALTERNATIVE_DOC,
                "divide_and_conquer_doc": DIVIDE_AND_CONQUER_DOC
            })
        except Exception as e:
            logger.exception(f"Error invoking LLM chain: {e}")
            # Get the original command from the act_result
            original_command = state.act_result[0].command if state.act_result else "echo 'No command found'"
            # デフォルトのCommandInputを作成
            cmd_input = CommandInput(
                command=original_command,
                timeout_sec=DEFAULT_TIMEOUT_SEC  # デフォルトのタイムアウト値
            )
            return GraphState(
                query=state.query,
                context=state.context,
                processed_query=state.processed_query,
                command_candidates=[cmd_input],
                generated_commands=state.generated_commands,
                is_retry=True,
                error_type="TIMEOUT",
                act_result=state.act_result
            )

        # Parse the result
        try:
            response_json = json.loads(result)

            # Extract commands and create CommandInput objects
            command_candidates = []

            for cmd_input in response_json.get("command_inputs", []):
                command = cmd_input.get("command", "")
                timeout_sec = cmd_input.get("timeout_sec")

                # タイムアウト値が設定されていることを確認
                assert timeout_sec is not None, f"タイムアウト値が設定されていません: {command}"

                if command:
                    # CommandInputオブジェクトを作成
                    command_input = CommandInput(
                        command=command,
                        timeout_sec=timeout_sec
                    )
                    command_candidates.append(command_input)

            if not command_candidates:
                logger.warning("No valid commands found in LLM response")
                # デフォルトのCommandInputを作成
                command_candidates = [CommandInput(
                    command="echo 'No valid commands generated'",
                    timeout_sec=DEFAULT_TIMEOUT_SEC  # デフォルトのタイムアウト値
                )]

            logger.info(f"Generated {len(command_candidates)} commands to handle timeout")

            # Update the state
            return GraphState(
                query=state.query,
                context=state.context,
                processed_query=state.processed_query,
                command_candidates=command_candidates,
                generated_commands=state.generated_commands,
                is_retry=True,
                error_type="TIMEOUT",
                act_result=state.act_result
            )
        except json.JSONDecodeError:
            logger.error(f"Failed to parse LLM response as JSON: {result}")
            # Return the original state with a fallback command
            return GraphState(
                query=state.query,
                context=state.context,
                processed_query=state.processed_query,
                command_candidates=[CommandInput(
                    command="echo 'Failed to generate timeout handling command'",
                    timeout_sec=DEFAULT_TIMEOUT_SEC  # デフォルトのタイムアウト値
                )],
                generated_commands=state.generated_commands,
                is_retry=True,
                error_type="TIMEOUT",
                act_result=state.act_result,
                api_error=True
            )
    except Exception as e:
        raise RuntimeError("Error handling timeout") from e
