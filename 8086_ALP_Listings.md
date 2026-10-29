# 8086 ALP listings (transcribed from supplied experiment)

The following is a readable transcription of the program text supplied with the experiment.
The trainer's assembler syntax and exact I/O map can vary. The source handout's byte listing
shows `OUT DX, AL`, a delay subroutine, and a rotate instruction. Confirm the rotate direction
and interface wiring against your instructor's kit before running on real hardware.

## Anticlockwise

```asm
ORG 6000H
A1:     MOV AL, 80H
        MOV DX, 0FFC6H
        OUT DX, AL
        MOV AL, 88H
        MOV DX, 0FFC4H
        OUT DX, AL
        CALL 6104H        ; DELAY
        ROL AL, 1
        JMP A1

; Delay routine at 6104H
        MOV CX, 2000H
A2:     LOOP A2
        RET
```

## Clockwise

```asm
ORG 6000H
A1:     MOV AL, 80H
        MOV DX, 0FFC6H
        OUT DX, AL
        MOV AL, 88H
        MOV DX, 0FFC4H
        OUT DX, AL
        CALL 6104H        ; DELAY
        ROR AL, 1
        JMP A1

; Delay routine at 6104H
        MOV CX, 2000H
A2:     LOOP A2
        RET
```

## Variable step-size in the virtual lab

The notebook exposes a **step size** control. It represents the number of electrical full-step
transitions applied for each requested movement unit. For example, 12 movement units with a
step size of 2 performs 24 simulated full-step transitions. The supplied handout's assembly
listing itself is a continuous loop and does not include an interactive keyboard step-size
routine; this feature is implemented in the software simulation.
