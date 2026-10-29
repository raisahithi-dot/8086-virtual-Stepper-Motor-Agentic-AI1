# Hardware notes from the supplied lab description

## Listed equipment
- 8086 trainer kit
- +5 V regulated supply
- 26-core FRC connector
- Stepper-motor interface module
- Stepper motor
- Keyboard

## Connection summary (verify with your trainer manual)
1. Connect the 26-core FRC cable between trainer connector CN4 and the interface module.
2. Connect the power-mate lead to the interface module and regulated supply.
3. The handout specifies black and red wires to GND, and blue and green wires to +5 V.
4. The handout's motor connector color mapping is:
   - A — Green
   - B — Green & White
   - C — Red & White
   - D — Red
   - VDD — Black & White

**Caution:** Wire colors and pinouts are not universal. Treat this as a transcription of the
provided handout, not an authoritative wiring diagram. Check the interface-module labels,
trainer-kit documentation, motor datasheet, supply polarity, and instructor instructions before
powering anything. Never connect a motor winding directly to an 8086 I/O pin; use the intended
driver/interface module.
