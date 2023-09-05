cwlVersion: v1.2
class: Workflow

requirements:
  InlineJavascriptRequirement: {}

inputs:
  message: string

outputs:
  out:
    type: string
    outputSource: uppercase/uppercase_message

steps:
  echo:
    run:
      class: CommandLineTool
      baseCommand: echo
      stdout: output.txt
      inputs:
        message:
          type: string
          inputBinding: {}
      outputs:
        out:
          type: string
          outputBinding:
            glob: output.txt
            loadContents: true
            outputEval: $(self[0].contents)
    in:
      message: message
    out: [out]
  uppercase:
    run:
      class: ExpressionTool
      inputs:
        message: string
      outputs:
        uppercase_message: string
      expression: |
        ${
          message = inputs["message"]
          uppercase_message = message.toUpperCase()
          return {"uppercase_message": uppercase_message}
        }
    in:
      message:
        source: echo/out
    out: [uppercase_message]
