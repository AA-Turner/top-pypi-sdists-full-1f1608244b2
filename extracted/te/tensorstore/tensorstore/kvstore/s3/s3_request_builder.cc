// Copyright 2023 The TensorStore Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifdef _WIN32
// openssl/boringssl may have conflicting macros with Windows.
#define WIN32_LEAN_AND_MEAN
#endif

#include "tensorstore/kvstore/s3/s3_request_builder.h"

#include <stddef.h>

#include <algorithm>
#include <cassert>
#include <string>
#include <string_view>
#include <utility>
#include <vector>

#include "absl/base/attributes.h"
#include "absl/log/absl_check.h"
#include "absl/log/absl_log.h"
#include "absl/strings/ascii.h"
#include "absl/strings/escaping.h"
#include "absl/strings/str_cat.h"
#include "absl/strings/str_format.h"
#include "absl/strings/str_join.h"
#include "absl/time/time.h"
#include <openssl/evp.h>  // IWYU pragma: keep
#include <openssl/hmac.h>
#include "tensorstore/internal/aws/aws_credentials.h"
#include "tensorstore/internal/digest/sha256.h"
#include "tensorstore/internal/http/http_request.h"
#include "tensorstore/internal/log/verbose_flag.h"
#include "tensorstore/internal/uri_utils.h"
#include "tensorstore/kvstore/s3/s3_uri_utils.h"

using ::tensorstore::internal::ParseGenericUri;
using ::tensorstore::internal::SHA256Digester;
using ::tensorstore::internal_aws::AwsCredentials;
using ::tensorstore::internal_http::HttpRequest;

namespace tensorstore {
namespace internal_kvstore_s3 {
namespace {

ABSL_CONST_INIT internal_log::VerboseFlag s3_logging("s3");

/// Size of HMAC (size of SHA256 digest).
constexpr static size_t kHmacSize = 32;

void ComputeHmac(std::string_view key, std::string_view message,
                 unsigned char (&hmac)[kHmacSize]) {
  unsigned int md_len = kHmacSize;
  // Computing HMAC should never fail.
  ABSL_CHECK(
      HMAC(EVP_sha256(), reinterpret_cast<const unsigned char*>(key.data()),
           key.size(), reinterpret_cast<const unsigned char*>(message.data()),
           message.size(), hmac, &md_len) &&
      md_len == kHmacSize);
}

void ComputeHmac(unsigned char (&key)[kHmacSize], std::string_view message,
                 unsigned char (&hmac)[kHmacSize]) {
  unsigned int md_len = kHmacSize;
  // Computing HMAC should never fail.
  ABSL_CHECK(HMAC(EVP_sha256(), key, kHmacSize,
                  reinterpret_cast<const unsigned char*>(message.data()),
                  message.size(), hmac, &md_len) &&
             md_len == kHmacSize);
}

/// https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-header-based-auth.html
std::string CanonicalRequest(
    std::string_view method, std::string_view path, std::string_view query,
    std::string_view payload_hash,
    const std::vector<std::pair<std::string, std::string_view>>& headers) {
  std::string canonical =
      absl::StrCat(method, "\n", S3UriObjectKeyEncode(path), "\n", query, "\n");

  // Canonical Headers
  std::vector<std::string_view> signed_headers;
  signed_headers.reserve(headers.size());
  for (auto& pair : headers) {
    absl::StrAppend(&canonical, pair.first, ":", pair.second, "\n");
    signed_headers.push_back(pair.first);
  }
  // Signed Headers
  absl::StrAppend(&canonical, "\n", absl::StrJoin(signed_headers, ";"), "\n",
                  payload_hash);
  return canonical;
}

std::string SigningString(std::string_view canonical_request,
                          const absl::Time& time, std::string_view scope) {
  absl::TimeZone utc = absl::UTCTimeZone();
  SHA256Digester sha256;
  sha256.Write(canonical_request);
  const auto digest = sha256.Digest();
  auto digest_sv = std::string_view(reinterpret_cast<const char*>(&digest[0]),
                                    digest.size());
  return absl::StrFormat("AWS4-HMAC-SHA256\n%s\n%s\n%s",
                         absl::FormatTime("%Y%m%dT%H%M%SZ", time, utc), scope,
                         absl::BytesToHexString(digest_sv));
}

void GetSigningKey(std::string_view aws_secret_access_key,
                   std::string_view aws_region, const absl::Time& time,
                   unsigned char (&signing_key)[kHmacSize]) {
  absl::TimeZone utc = absl::UTCTimeZone();
  unsigned char date_key[kHmacSize];
  unsigned char date_region_key[kHmacSize];
  unsigned char date_region_service_key[kHmacSize];

  ComputeHmac(absl::StrCat("AWS4", aws_secret_access_key),
              absl::FormatTime("%Y%m%d", time, utc), date_key);
  ComputeHmac(date_key, aws_region, date_region_key);
  ComputeHmac(date_region_key, "s3", date_region_service_key);
  ComputeHmac(date_region_service_key, "aws4_request", signing_key);
}

std::string AuthorizationHeader(
    std::string_view access_key, std::string_view scope,
    std::string_view signature_hex,
    const std::vector<std::pair<std::string, std::string_view>>& headers) {
  return absl::StrFormat(
      "AWS4-HMAC-SHA256 "
      "Credential=%s/%s, "
      "SignedHeaders=%s, "
      "Signature=%s",
      access_key, scope,
      absl::StrJoin(headers, ";",
                    [](std::string* out, auto pair) {
                      absl::StrAppend(out, pair.first);
                    }),
      signature_hex);
}

static constexpr char kAmzContentSha256Header[] = "x-amz-content-sha256";
static constexpr char kAmzSecurityTokenHeader[] = "x-amz-security-token";

}  // namespace

// https://docs.aws.amazon.com/AmazonS3/latest/userguide/ObjectsinRequesterPaysBuckets.html
// For DELETE, GET, HEAD, POST, and PUT requests, include
// x-amz-request-payer : requester in the header
S3RequestBuilder& S3RequestBuilder::MaybeAddRequesterPayer(
    bool requester_payer) {
  if (requester_payer) {
    builder_.AddHeader("x-amz-requester-payer", "requester");
  }
  return *this;
}

HttpRequest S3RequestBuilder::BuildRequest(std::string_view host_header,
                                           const AwsCredentials& credentials,
                                           std::string_view aws_region,
                                           std::string_view payload_sha256_hash,
                                           const absl::Time& time) {
  builder_.AddHostHeader(host_header);
  builder_.AddHeader(kAmzContentSha256Header, payload_sha256_hash);
  builder_.AddHeader("x-amz-date", absl::FormatTime("%Y%m%dT%H%M%SZ", time,
                                                    absl::UTCTimeZone()));

  // Add deferred query parameters in sorted order for AWS4 signature
  // requirements
  std::stable_sort(std::begin(query_params_), std::end(query_params_));
  for (const auto& [k, v] : query_params_) {
    builder_.AddQueryParameter(k, v);
  }

  // If anonymous, it's unnecessary to construct the Authorization header
  if (credentials.IsAnonymous()) {
    return builder_.BuildRequest();
  }

  // Add AWS Session Token, if available
  // https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html#UsingTemporarySecurityCredentials
  if (auto session_token = credentials.GetSessionToken();
      !session_token.empty()) {
    builder_.AddHeader(kAmzSecurityTokenHeader, session_token);
  }

  auto request = builder_.BuildRequest();

  // Create sorted AWS4 signing headers
  std::vector<std::pair<std::string, std::string_view>> signed_headers;
  signed_headers.reserve(request.headers.size());
  for (const auto& kv : request.headers) {
    std::string key = absl::AsciiStrToLower(kv.first);
    std::string_view value = absl::StripAsciiWhitespace(kv.second);
    signed_headers.push_back({std::move(key), std::move(value)});
  }

  auto parsed_uri = ParseGenericUri(request.url);
  assert(!parsed_uri.path.empty());

  std::string scope = absl::StrFormat(
      "%s/%s/s3/aws4_request",
      absl::FormatTime("%Y%m%d", time, absl::UTCTimeZone()), aws_region);

  canonical_request_ =
      CanonicalRequest(request.method, parsed_uri.path, parsed_uri.query,
                       payload_sha256_hash, signed_headers);
  signing_string_ = SigningString(canonical_request_, time, scope);

  unsigned char signing_key[kHmacSize];
  GetSigningKey(credentials.GetSecretAccessKey(), aws_region, time,
                signing_key);

  unsigned char signature[kHmacSize];
  ComputeHmac(signing_key, signing_string_, signature);
  signature_ = absl::BytesToHexString(
      std::string_view(reinterpret_cast<char*>(&signature[0]), kHmacSize));

  std::string auth_header = AuthorizationHeader(
      credentials.GetAccessKeyId(), scope, signature_, signed_headers);

  ABSL_LOG_IF(INFO, s3_logging.Level(1))  //
      << "Canonical Request\n"
      << canonical_request_  //
      << "\n\nSigning String\n"
      << signing_string_      //
      << "\n\nSigning Key\n"  //
      << absl::BytesToHexString(std::string_view(
             reinterpret_cast<char*>(signing_key), kHmacSize))  //
      << "\n\nAuthorization Header\n"
      << auth_header;

  request.headers.SetHeader("authorization", auth_header);
  return request;
}

}  // namespace internal_kvstore_s3
}  // namespace tensorstore
