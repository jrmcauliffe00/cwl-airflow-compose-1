cwlVersion: v1.0
class: Workflow

inputs:
  message:
    type: string

outputs:
  echoStdOut:
    type: File
    outputSource: echo/echoStdOut
  echoStdErr:
    type: File
    outputSource: echo/echoStdErr

steps:
  echo:
    run:
      cwlVersion: v1.0
      id: echo
      class: CommandLineTool
      requirements:
        - class: DockerRequirement
          dockerPull: busybox
      baseCommand: echo
      stdout: echo.out
      stderr: echo.err
      inputs:
        message:
          type: string
          inputBinding:
            position: 1
      outputs:
        echoStdOut:
          type: stdout
        echoStdErr:
          type: stderr
    in:
      message: message
    out:
      - echoStdOut
      - echoStdErr
