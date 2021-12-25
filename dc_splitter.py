# = Public Domain =============================================================
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <https://unlicense.org>
# =============================================================================

default_char_limit = 2000

# splits string by a character limit
# if possible, splits by given characters without exceeding the character limit
# erases leading (starting & ending) characters from the created splits if needed
# ignores text formatting, see: splitCode() for code formatting
def splitText(
        text : str,
        char_limit : int = default_char_limit,
        split_by : list = ['\n', ' ', '.', ','],
        erase_leadings : list = ['\n', ' ']
    ) -> list:

    subtexts = []
    index = 0
    while index < len(text):
        cut_size = char_limit

        # end of string - no need for a split
        if index + char_limit >= len(text):
            cut_size = len(text) - index

        # split
        else:
            # find a split character moving to the left from char_limit
            # I've seen people turn their heads...
            #      <-|    (split_by ' ', char_limit = 7)
            #
            # do it for each character, if neither is found, split at char_limit
            for split_char in split_by:
                split_index = text.rfind(split_char, index, index + cut_size)

                # limit found - fix cut size
                if split_index != -1:
                    cut_size = split_index - index + 1
                    break

        # ignore leadings
        # ._.And quickly._ look awa.y.
        #        \/                        (erase_leadings = ['.', '_'])
        # And quickly._ look awa.y
        begin_index, end_index = index, index + cut_size

        find_index = begin_index
        while find_index != end_index and text[find_index] in erase_leadings:
            find_index += 1
        begin_index = find_index

        find_index = end_index - 1
        while find_index != begin_index - 1 and text[find_index] in erase_leadings:
            find_index -= 1
        end_index = find_index + 1

        # cache substring
        if begin_index != end_index:
            subtexts.append(text[begin_index : end_index])
        index += cut_size

    return subtexts

# splits unformatted code into several code blocks
# ```<language_filename>
# for (auto it(vec.begin()); it != vec.end(); it++)
#        it->Update();
# ```
def splitCode(code : str, language_filename : str = "", char_limit : int = default_char_limit) -> list:

    # ensure code can fit inside formatting
    # ```<language_filename>
    # <code>
    # ```
    format_start, format_end = f"```{language_filename}\n", "```"
    format_length = len(format_start) + len(format_end)

    if format_length >= char_limit:
        raise Exception("Character limit set too low, could not fit both code and formatting")

    # offset character limit by needed formatting
    # and split the code into blocks
    code_blocks = splitText(code, char_limit - format_length, split_by = ['\n'], erase_leadings = [])

    # include the formatting
    for index, block in enumerate(code_blocks):
        if "```" in block:
            raise Exception("'```' code formatting sequence has been found, unable to split the code")

        code_blocks[index] = format_start + block + format_end

    return code_blocks
