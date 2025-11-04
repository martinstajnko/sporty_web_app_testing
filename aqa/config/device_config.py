"""Device configuration for different viewports."""

from typing import Any, Dict

from aqa.utils.enums import DeviceType


class DeviceConfig:
    """Provides device viewport configurations."""

    CONFIGS = {
        DeviceType.DESKTOP: {
            "viewport": {
                "width": 1920,
                "height": 1080,
            },
        },
        DeviceType.MOBILE: {
            "viewport": {
                "width": 375,
                "height": 667,
            },
            "device_scale_factor": 2,
            "is_mobile": True,
            "has_touch": True,
        },
        DeviceType.TABLET: {
            "viewport": {
                "width": 768,
                "height": 1024,
            },
            "device_scale_factor": 2,
            "is_mobile": True,
            "has_touch": True,
        },
    }

    @staticmethod
    def get_context_options(device_type: DeviceType) -> Dict[str, Any]:
        """Get browser context options for device type."""
        return DeviceConfig.CONFIGS.get(
            device_type, DeviceConfig.CONFIGS[DeviceType.DESKTOP]
        )
