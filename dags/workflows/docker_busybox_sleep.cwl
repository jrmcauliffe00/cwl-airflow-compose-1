
cwlVersion: v1.0
class: Workflow

inputs:
  sleepParam: string
outputs: {}

steps:
  sleep:
    run:
      cwlVersion: v1.0
      id: sleep
      class: CommandLineTool
      requirements:
        DockerRequirement:
          dockerPull: busybox
      baseCommand:
        - sleep
      inputs:
        sleepParam:
          type: string
          inputBinding:
            position: 1
      outputs:
        sleepStdOut:
          type: stdout
        sleepStdErr:
          type: stderr
    in:
      sleepParam: sleepParam
    out: []
