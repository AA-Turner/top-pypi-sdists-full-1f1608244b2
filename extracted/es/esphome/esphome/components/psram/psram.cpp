
#ifdef USE_ESP32
#include "psram.h"
#include <esp_idf_version.h>
#if defined(USE_ESP_IDF) && ESP_IDF_VERSION_MAJOR >= 5
#include <esp_psram.h>
#endif  // USE_ESP_IDF

#include "esphome/core/log.h"

#include <esp_heap_caps.h>

namespace esphome {
namespace psram {
static const char *const TAG = "psram";

void PsramComponent::dump_config() {
  ESP_LOGCONFIG(TAG, "PSRAM:");
#if defined(USE_ESP_IDF) && ESP_IDF_VERSION_MAJOR >= 5
  bool available = esp_psram_is_initialized();

  ESP_LOGCONFIG(TAG, "  Available: %s", YESNO(available));
  if (available) {
    ESP_LOGCONFIG(TAG, "  Size: %zu KB", esp_psram_get_size() / 1024);
#if CONFIG_SPIRAM_ECC_ENABLE
    ESP_LOGCONFIG(TAG, "  ECC enabled: YES");
#endif
  }
#else
  // Technically this can be false if the PSRAM is full, but heap_caps_get_total_size() isn't always available, and it's
  // very unlikely for the PSRAM to be full.
  bool available = heap_caps_get_free_size(MALLOC_CAP_SPIRAM) > 0;
  ESP_LOGCONFIG(TAG, "  Available: %s", YESNO(available));

  if (available) {
    const size_t psram_total_size_bytes = heap_caps_get_total_size(MALLOC_CAP_SPIRAM);
    const float psram_total_size_kb = psram_total_size_bytes / 1024.0f;

    if (abs(std::round(psram_total_size_kb) - psram_total_size_kb) < 0.05f) {
      ESP_LOGCONFIG(TAG, "  Size: %.0f KB", psram_total_size_kb);
    } else {
      ESP_LOGCONFIG(TAG, "  Size: %zu bytes", psram_total_size_bytes);
    }
  }
#endif  // USE_ESP_IDF
}

}  // namespace psram
}  // namespace esphome

#endif
