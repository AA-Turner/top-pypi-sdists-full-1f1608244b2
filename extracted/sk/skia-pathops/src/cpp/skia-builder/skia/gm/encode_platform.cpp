/*
 * Copyright 2016 Google Inc.
 *
 * Use of this source code is governed by a BSD-style license that can be
 * found in the LICENSE file.
 */

#include "gm/gm.h"
#include "include/codec/SkEncodedImageFormat.h"
#include "include/core/SkBitmap.h"
#include "include/core/SkCanvas.h"
#include "include/core/SkData.h"
#include "include/core/SkImage.h"
#include "include/core/SkImageInfo.h"
#include "include/core/SkPixmap.h"
#include "include/core/SkRect.h"
#include "include/core/SkRefCnt.h"
#include "include/core/SkSize.h"
#include "include/core/SkStream.h"
#include "include/core/SkString.h"
#include "include/core/SkTypes.h"
#include "include/encode/SkJpegEncoder.h"
#include "include/encode/SkPngEncoder.h"
#include "include/encode/SkWebpEncoder.h"
#include "tools/Resources.h"

#if defined(SK_BUILD_FOR_MAC) || defined(SK_BUILD_FOR_IOS) || defined(SK_BUILD_FOR_WIN) \
 || defined(SK_ENABLE_NDK_IMAGES)
#include "src/encode/SkImageEncoderPriv.h"
#endif

namespace {

static const struct {
    SkEncodedImageFormat format;
    int                  quality;
} gRecs[] = {
#if defined(SK_BUILD_FOR_MAC) || defined(SK_BUILD_FOR_IOS)
    { SkEncodedImageFormat::kPNG,  100},
    { SkEncodedImageFormat::kJPEG, 100},
    { SkEncodedImageFormat::kGIF,  100},
    { SkEncodedImageFormat::kBMP,  100},
    { SkEncodedImageFormat::kICO,  100},
#elif defined(SK_BUILD_FOR_WIN)
    // Our WIC encoder does not support GIF, BMP, or ICO.
    { SkEncodedImageFormat::kPNG,  100},
    { SkEncodedImageFormat::kJPEG, 100},
    { SkEncodedImageFormat::kPNG,  100},
    { SkEncodedImageFormat::kPNG,  100},
    { SkEncodedImageFormat::kPNG,  100},
#else
    // We don't support GIF, BMP, or ICO. This applies to both NDK and SkEncoder.
    { SkEncodedImageFormat::kPNG,  100},
    { SkEncodedImageFormat::kJPEG, 100},
    { SkEncodedImageFormat::kWEBP, 100}, // Lossless
    { SkEncodedImageFormat::kWEBP,  80}, // Lossy
    { SkEncodedImageFormat::kPNG,  100},
#endif
};

} // anonymous namespace

static sk_sp<SkData> encode_data(SkEncodedImageFormat type, const SkBitmap& bitmap, int quality) {
    SkPixmap src;
    if (!bitmap.peekPixels(&src)) {
        return nullptr;
    }
    SkDynamicMemoryWStream buf;
    #if defined(SK_BUILD_FOR_MAC) || defined(SK_BUILD_FOR_IOS)
        return SkEncodeImageWithCG(&buf, src, type) ? buf.detachAsData() : nullptr;
    #elif defined(SK_BUILD_FOR_WIN)
        return SkEncodeImageWithWIC(&buf, src, type, quality) ? buf.detachAsData() : nullptr;
    #elif defined(SK_ENABLE_NDK_IMAGES)
        return SkEncodeImageWithNDK(&buf, src, type, quality) ? buf.detachAsData() : nullptr;
    #else
        switch (type) {
            case SkEncodedImageFormat::kPNG: {
                bool success = SkPngEncoder::Encode(&buf, src, SkPngEncoder::Options());
                return success ? buf.detachAsData() : nullptr;
            }
            case SkEncodedImageFormat::kJPEG: {
                bool success = SkJpegEncoder::Encode(&buf, src, SkJpegEncoder::Options());
                return success ? buf.detachAsData() : nullptr;
            }
            case SkEncodedImageFormat::kWEBP: {
                bool success = SkWebpEncoder::Encode(&buf, src, SkWebpEncoder::Options());
                return success ? buf.detachAsData() : nullptr;
            }
            default:
                SkUNREACHABLE;
        }
    #endif
}

namespace skiagm {

class EncodePlatformGM : public GM {
public:
    EncodePlatformGM() {}

protected:
    SkString onShortName() override {
        return SkString("encode-platform");
    }

    SkISize onISize() override {
        return SkISize::Make(256 * std::size(gRecs), 256 * 3);
    }

    DrawResult onDraw(SkCanvas* canvas, SkString* errorMsg) override {
        SkBitmap opaqueBm, premulBm, unpremulBm;

        if (!GetResourceAsBitmap("images/mandrill_256.png", &opaqueBm)) {
            *errorMsg = "Could not load images/mandrill_256.png.png. "
                        "Did you forget to set the resourcePath?";
            return DrawResult::kFail;
        }
        SkBitmap tmp;
        if (!GetResourceAsBitmap("images/yellow_rose.png", &tmp)) {
            *errorMsg = "Could not load images/yellow_rose.png. "
                        "Did you forget to set the resourcePath?";
            return DrawResult::kFail;
        }
        tmp.extractSubset(&premulBm, SkIRect::MakeWH(256, 256));
        tmp.reset();
        unpremulBm.allocPixels(premulBm.info().makeAlphaType(kUnpremul_SkAlphaType));
        SkAssertResult(premulBm.readPixels(unpremulBm.pixmap()));

        for (const auto& rec : gRecs) {
            auto fmt = rec.format; int q = rec.quality;
            auto opaqueImage   = SkImage::MakeFromEncoded(encode_data(fmt, opaqueBm,   q));
            auto premulImage   = SkImage::MakeFromEncoded(encode_data(fmt, premulBm,   q));
            auto unpremulImage = SkImage::MakeFromEncoded(encode_data(fmt, unpremulBm, q));

            canvas->drawImage(opaqueImage.get(), 0.0f, 0.0f);
            canvas->drawImage(premulImage.get(), 0.0f, 256.0f);
            canvas->drawImage(unpremulImage.get(), 0.0f, 512.0f);

            canvas->translate(256.0f, 0.0f);
        }
        return DrawResult::kOk;
    }

private:
    using INHERITED = GM;
};

DEF_GM( return new EncodePlatformGM; )
}  // namespace skiagm
