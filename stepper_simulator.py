"""Educational 4-state stepper motor simulation for an 8086 lab exercise."""
from dataclasses import dataclass, field

SEQUENCE = (0b1000, 0b0100, 0b0010, 0b0001)

@dataclass
class StepperMotor:
    """Tracks electrical state and accumulated full-step position."""
    state_index: int = 0
    position_steps: int = 0
    history: list = field(default_factory=list)

    def move(self, direction: str, steps: int):
        direction = direction.lower()
        if direction not in {"clockwise", "anticlockwise"}:
            raise ValueError("direction must be 'clockwise' or 'anticlockwise'")
        if not isinstance(steps, int) or steps < 1:
            raise ValueError("steps must be a positive integer")
        delta = 1 if direction == "clockwise" else -1
        events = []
        for _ in range(steps):
            self.state_index = (self.state_index + delta) % len(SEQUENCE)
            self.position_steps += delta
            pattern = SEQUENCE[self.state_index]
            event = {
                "direction": direction,
                "state": self.state_index,
                "pattern": f"{pattern:04b}",
                "position_steps": self.position_steps,
            }
            self.history.append(event)
            events.append(event)
        return events

def assembly_listing(direction: str) -> str:
    """Return a readable transcription of the supplied 8086 lab-manual program."""
    direction = direction.lower()
    if direction == "anticlockwise":
        rotate = "ROL AL, 1"
    elif direction == "clockwise":
        rotate = "ROR AL, 1"
    else:
        raise ValueError("direction must be 'clockwise' or 'anticlockwise'")
    return f"""ORG 6000H
START:  MOV AL, 80H
        MOV DX, 0FFC6H
        OUT DX, AL
        MOV AL, 88H
        MOV DX, 0FFC4H
        OUT DX, AL
        CALL DELAY
        {rotate}
        JMP START

; Delay routine (placed at 6104H in the lab listing)
DELAY:  MOV CX, 2000H
WAIT:   LOOP WAIT
        RET
"""
