from esphome import automation
from esphome.automation import maybe_simple_id
import esphome.codegen as cg
from esphome.components import sensor, uart
import esphome.config_validation as cv
from esphome.const import (
    CONF_CO2,
    CONF_ID,
    CONF_TEMPERATURE,
    DEVICE_CLASS_CARBON_DIOXIDE,
    DEVICE_CLASS_TEMPERATURE,
    ICON_MOLECULE_CO2,
    STATE_CLASS_MEASUREMENT,
    UNIT_CELSIUS,
    UNIT_PARTS_PER_MILLION,
)

DEPENDENCIES = ["uart"]

CONF_AUTOMATIC_BASELINE_CALIBRATION = "automatic_baseline_calibration"
CONF_WARMUP_TIME = "warmup_time"

mhz19_ns = cg.esphome_ns.namespace("mhz19")
MHZ19Component = mhz19_ns.class_("MHZ19Component", cg.PollingComponent, uart.UARTDevice)
MHZ19CalibrateZeroAction = mhz19_ns.class_(
    "MHZ19CalibrateZeroAction", automation.Action
)
MHZ19ABCEnableAction = mhz19_ns.class_("MHZ19ABCEnableAction", automation.Action)
MHZ19ABCDisableAction = mhz19_ns.class_("MHZ19ABCDisableAction", automation.Action)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(MHZ19Component),
            cv.Optional(CONF_CO2): sensor.sensor_schema(
                unit_of_measurement=UNIT_PARTS_PER_MILLION,
                icon=ICON_MOLECULE_CO2,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_CARBON_DIOXIDE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_AUTOMATIC_BASELINE_CALIBRATION): cv.boolean,
            cv.Optional(
                CONF_WARMUP_TIME, default="75s"
            ): cv.positive_time_period_seconds,
        }
    )
    .extend(cv.polling_component_schema("60s"))
    .extend(uart.UART_DEVICE_SCHEMA)
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if co2 := config.get(CONF_CO2):
        sens = await sensor.new_sensor(co2)
        cg.add(var.set_co2_sensor(sens))

    if temperature := config.get(CONF_TEMPERATURE):
        sens = await sensor.new_sensor(temperature)
        cg.add(var.set_temperature_sensor(sens))

    if (
        automatic_baseline_calibration := config.get(
            CONF_AUTOMATIC_BASELINE_CALIBRATION
        )
    ) is not None:
        cg.add(var.set_abc_enabled(automatic_baseline_calibration))

    cg.add(var.set_warmup_seconds(config[CONF_WARMUP_TIME]))


CALIBRATION_ACTION_SCHEMA = maybe_simple_id(
    {
        cv.Required(CONF_ID): cv.use_id(MHZ19Component),
    }
)


@automation.register_action(
    "mhz19.calibrate_zero", MHZ19CalibrateZeroAction, CALIBRATION_ACTION_SCHEMA
)
@automation.register_action(
    "mhz19.abc_enable", MHZ19ABCEnableAction, CALIBRATION_ACTION_SCHEMA
)
@automation.register_action(
    "mhz19.abc_disable", MHZ19ABCDisableAction, CALIBRATION_ACTION_SCHEMA
)
async def mhz19_calibration_to_code(config, action_id, template_arg, args):
    paren = await cg.get_variable(config[CONF_ID])
    return cg.new_Pvariable(action_id, template_arg, paren)
