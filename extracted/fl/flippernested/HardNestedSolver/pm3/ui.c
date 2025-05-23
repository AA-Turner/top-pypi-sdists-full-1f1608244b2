//-----------------------------------------------------------------------------
// Copyright (C) Proxmark3 contributors. See AUTHORS.md for details.
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// See LICENSE.txt for the text of the license.
//-----------------------------------------------------------------------------
// UI utilities
//-----------------------------------------------------------------------------

/* Ensure strtok_r is available even with -std=c99; must be included before
 */

#include "ui.h"
#include "commonutil.h"  // ARRAYLEN
#include <stdio.h> // for Mingw readline
#include <stdarg.h>
#include <stdlib.h>

#if defined(HAVE_READLINE)
//Load readline after stdio.h
#include <readline/readline.h>
#endif

#include "util.h"

#ifdef _WIN32
# include <direct.h>    // _mkdir
#endif

#include "emojis.h"
#include "emojis_alt.h"
#include <string.h>

session_arg_t g_session;

static bool flushAfterWrite = false;
static void fPrintAndLog(FILE *stream, const char *fmt, ...);

#ifdef _WIN32
#define MKDIR_CHK _mkdir(path)
#define STRTOK strtok
#else
#define MKDIR_CHK mkdir(path, 0700)
#define STRTOK strtok_r
#endif

static uint8_t PrintAndLogEx_spinidx = 0;

void PrintAndLogEx(logLevel_t level, const char *fmt, ...) {

    // skip debug messages if client debugging is turned off i.e. 'DATA SETDEBUG -0'
    if (g_debugMode == 0 && level == DEBUG)
        return;

    // skip HINT messages if client has hints turned off i.e. 'HINT 0'
    if (g_session.show_hints == false && level == HINT)
        return;

    char prefix[40] = {0};
    char buffer[MAX_PRINT_BUFFER] = {0};
    char buffer2[MAX_PRINT_BUFFER + sizeof(prefix)] = {0};
    char *token = NULL;
    char *tmp_ptr = NULL;
    FILE *stream = stdout;
    const char *spinner[] = {_YELLOW_("[\\]"), _YELLOW_("[|]"), _YELLOW_("[/]"), _YELLOW_("[-]")};
    const char *spinner_emoji[] = {" :clock1: ", " :clock2: ", " :clock3: ", " :clock4: ", " :clock5: ", " :clock6: ",
                                   " :clock7: ", " :clock8: ", " :clock9: ", " :clock10: ", " :clock11: ",
                                   " :clock12: "};
    switch (level) {
        case ERR:
            if (g_session.emoji_mode == EMO_EMOJI)
                strncpy(prefix, "[" _RED_("!!") "] :rotating_light: ", sizeof(prefix) - 1);
            else
                strncpy(prefix, "[" _RED_("!!") "] ", sizeof(prefix) - 1);
            stream = stderr;
            break;
        case FAILED:
            if (g_session.emoji_mode == EMO_EMOJI)
                strncpy(prefix, "[" _RED_("-") "] :no_entry: ", sizeof(prefix) - 1);
            else
                strncpy(prefix, "[" _RED_("-") "] ", sizeof(prefix) - 1);
            break;
        case DEBUG:
            strncpy(prefix, "[" _BLUE_("#") "] ", sizeof(prefix) - 1);
            break;
        case HINT:
            strncpy(prefix, "[" _YELLOW_("?") "] ", sizeof(prefix) - 1);
            break;
        case SUCCESS:
            strncpy(prefix, "[" _GREEN_("+") "] ", sizeof(prefix) - 1);
            break;
        case WARNING:
            if (g_session.emoji_mode == EMO_EMOJI)
                strncpy(prefix, "[" _CYAN_("!") "] :warning:  ", sizeof(prefix) - 1);
            else
                strncpy(prefix, "[" _CYAN_("!") "] ", sizeof(prefix) - 1);
            break;
        case INFO:
            strncpy(prefix, "[" _YELLOW_("=") "] ", sizeof(prefix) - 1);
            break;
        case INPLACE:
            if (g_session.emoji_mode == EMO_EMOJI) {
                strncpy(prefix, spinner_emoji[PrintAndLogEx_spinidx], sizeof(prefix) - 1);
                PrintAndLogEx_spinidx++;
                if (PrintAndLogEx_spinidx >= ARRAYLEN(spinner_emoji))
                    PrintAndLogEx_spinidx = 0;
            } else {
                strncpy(prefix, spinner[PrintAndLogEx_spinidx], sizeof(prefix) - 1);
                PrintAndLogEx_spinidx++;
                if (PrintAndLogEx_spinidx >= ARRAYLEN(spinner))
                    PrintAndLogEx_spinidx = 0;
            }
            break;
        case NORMAL:
            // no prefixes for normal
            break;
    }

    va_list args;
    va_start(args, fmt);
    vsnprintf(buffer, sizeof(buffer), fmt, args);
    va_end(args);

    // no prefixes for normal & inplace
    if (level == NORMAL) {
        fPrintAndLog(stream, "%s", buffer);
        return;
    }

    if (strchr(buffer, '\n')) {

        const char delim[2] = "\n";

        // line starts with newline
        if (buffer[0] == '\n')
            fPrintAndLog(stream, "");

        token = STRTOK(buffer, delim, &tmp_ptr);

        while (token != NULL) {

            size_t size = strlen(buffer2);

            if (strlen(token))
                snprintf(buffer2 + size, sizeof(buffer2) - size, "%s%s\n", prefix, token);
            else
                snprintf(buffer2 + size, sizeof(buffer2) - size, "\n");

            token = STRTOK(NULL, delim, &tmp_ptr);
        }
        fPrintAndLog(stream, "%s", buffer2);
    } else {
        snprintf(buffer2, sizeof(buffer2), "%s%s", prefix, buffer);
        if (level == INPLACE) {
            char buffer3[sizeof(buffer2)] = {0};
            char buffer4[sizeof(buffer2)] = {0};
            memcpy_filter_ansi(buffer3, buffer2, sizeof(buffer2), !g_session.supports_colors);
            memcpy_filter_emoji(buffer4, buffer3, sizeof(buffer3), g_session.emoji_mode);
            fprintf(stream, "\r%s", buffer4);
            fflush(stream);
        } else {
            fPrintAndLog(stream, "%s", buffer2);
        }
    }
}

static void fPrintAndLog(FILE *stream, const char *fmt, ...) {
    va_list argptr;
    static FILE *logfile = NULL;
    static int logging = 1;
    char buffer[MAX_PRINT_BUFFER] = {0};
    char buffer2[MAX_PRINT_BUFFER] = {0};
    char buffer3[MAX_PRINT_BUFFER] = {0};
    // lock this section to avoid interlacing prints from different threads
    bool linefeed = true;

    logging = 0;


// If there is an incoming message from the hardware (eg: lf hid read) in
// the background (while the prompt is displayed and accepting user input),
// stash the prompt and bring it back later.
#ifdef RL_STATE_READCMD
    // We are using GNU readline. libedit (OSX) doesn't support this flag.
    int need_hack = (rl_readline_state & RL_STATE_READCMD) > 0;
    char *saved_line;
    int saved_point;

    if (need_hack) {
        saved_point = rl_point;
        saved_line = rl_copy_text(0, rl_end);
        rl_save_prompt();
        rl_replace_line("", 0);
        rl_redisplay();
    }
#endif

    va_start(argptr, fmt);
    vsnprintf(buffer, sizeof(buffer), fmt, argptr);
    va_end(argptr);
    if (strlen(buffer) > 0 && buffer[strlen(buffer) - 1] == NOLF[0]) {
        linefeed = false;
        buffer[strlen(buffer) - 1] = 0;
    }
    bool filter_ansi = !g_session.supports_colors;
    memcpy_filter_ansi(buffer2, buffer, sizeof(buffer), filter_ansi);
    if (g_printAndLog & PRINTANDLOG_PRINT) {
        memcpy_filter_emoji(buffer3, buffer2, sizeof(buffer2), g_session.emoji_mode);
        fprintf(stream, "%s", buffer3);
        if (linefeed)
            fprintf(stream, "\n");
    }

#ifdef RL_STATE_READCMD
    // We are using GNU readline. libedit (OSX) doesn't support this flag.
    if (need_hack) {
        rl_restore_prompt();
        rl_replace_line(saved_line, 0);
        rl_point = saved_point;
        rl_redisplay();
        free(saved_line);
    }
#endif

    if ((g_printAndLog & PRINTANDLOG_LOG) && logging && logfile) {
        memcpy_filter_emoji(buffer3, buffer2, sizeof(buffer2), EMO_ALTTEXT);
        if (filter_ansi) { // already done
            fprintf(logfile, "%s", buffer3);
        } else {
            memcpy_filter_ansi(buffer, buffer3, sizeof(buffer3), true);
            fprintf(logfile, "%s", buffer);
        }
        if (linefeed)
            fprintf(logfile, "\n");
        fflush(logfile);
    }

    if (flushAfterWrite)
        fflush(stdout);
}

void memcpy_filter_ansi(void *dest, const void *src, size_t n, bool filter) {
    if (filter) {
        // Filter out ANSI sequences on these OS
        uint8_t *rdest = (uint8_t *) dest;
        uint8_t *rsrc = (uint8_t *) src;
        uint16_t si = 0;
        for (size_t i = 0; i < n; i++) {
            if ((i < n - 1) && (rsrc[i] == '\x1b') && (rsrc[i + 1] >= 0x40) &&
                (rsrc[i + 1] <= 0x5F)) {  // entering ANSI sequence

                i++;
                if ((i < n - 1) && (rsrc[i] == '[')) { // entering CSI sequence
                    i++;

                    while ((i < n - 1) && (rsrc[i] >= 0x30) && (rsrc[i] <= 0x3F)) { // parameter bytes
                        i++;
                    }

                    while ((i < n - 1) && (rsrc[i] >= 0x20) && (rsrc[i] <= 0x2F)) { // intermediate bytes
                        i++;
                    }

                    if ((rsrc[i] >= 0x40) && (rsrc[i] <= 0x7F)) { // final byte
                        continue;
                    }
                } else {
                    continue;
                }
            }
            rdest[si++] = rsrc[i];
        }
    } else {
        memcpy(dest, src, n);
    }
}

static bool
emojify_token(const char *token, uint8_t token_length, const char **emojified_token, uint8_t *emojified_token_length,
              emojiMode_t mode) {
    int i = 0;
    while (EmojiTable[i].alias && EmojiTable[i].emoji) {
        if ((strlen(EmojiTable[i].alias) == token_length) && (0 == memcmp(EmojiTable[i].alias, token, token_length))) {
            switch (mode) {
                case EMO_EMOJI: {
                    *emojified_token = EmojiTable[i].emoji;
                    *emojified_token_length = strlen(EmojiTable[i].emoji);
                    break;
                }
                case EMO_ALTTEXT: {
                    int j = 0;
                    *emojified_token_length = 0;
                    while (EmojiAltTable[j].alias && EmojiAltTable[j].alttext) {
                        if ((strlen(EmojiAltTable[j].alias) == token_length) &&
                            (0 == memcmp(EmojiAltTable[j].alias, token, token_length))) {
                            *emojified_token = EmojiAltTable[j].alttext;
                            *emojified_token_length = strlen(EmojiAltTable[j].alttext);
                            break;
                        }
                        ++j;
                    }
                    break;
                }
                case EMO_NONE: {
                    *emojified_token_length = 0;
                    break;
                }
                case EMO_ALIAS: { // should never happen
                    return false;
                }
            }
            return true;
        }
        ++i;
    }
    return false;
}

static bool token_charset(uint8_t c) {
    if ((c >= '0') && (c <= '9')) return true;
    if ((c >= 'a') && (c <= 'z')) return true;
    if ((c >= 'A') && (c <= 'Z')) return true;
    if ((c == '_') || (c == '+') || (c == '-')) return true;
    return false;
}

void memcpy_filter_emoji(void *dest, const void *src, size_t n, emojiMode_t mode) {
    if (mode == EMO_ALIAS) {
        memcpy(dest, src, n);
    } else {
        // tokenize emoji
        const char *emojified_token = NULL;
        uint8_t emojified_token_length = 0;
        char *current_token = NULL;
        uint8_t current_token_length = 0;
        char *rdest = (char *) dest;
        char *rsrc = (char *) src;
        uint16_t si = 0;
        for (size_t i = 0; i < n; i++) {
            char current_char = rsrc[i];

            if (current_token_length == 0) {
                // starting a new token.
                if (current_char == ':') {
                    current_token = rsrc + i;
                    current_token_length = 1;
                } else { // not starting a new token.
                    rdest[si++] = current_char;
                }
            } else {
                // finishing the current token.
                if (current_char == ':') {
                    // nothing changed? we still need the ending ':' as it might serve for an upcoming emoji
                    if (!emojify_token(current_token, current_token_length + 1, &emojified_token,
                                       &emojified_token_length, mode)) {
                        memcpy(rdest + si, current_token, current_token_length);
                        si += current_token_length;
                        current_token = rsrc + i;
                        current_token_length = 1;
                    } else {
                        memcpy(rdest + si, emojified_token, emojified_token_length);
                        si += emojified_token_length;
                        current_token_length = 0;
                    }
                } else if (token_charset(current_char)) { // continuing the current token.
                    current_token_length++;
                } else { // dropping the current token.
                    current_token_length++;
                    memcpy(rdest + si, current_token, current_token_length);
                    si += current_token_length;
                    current_token_length = 0;
                }
            }
        }
        if (current_token_length > 0) {
            memcpy(rdest + si, current_token, current_token_length);
        }
    }
}