# Keyboard macro to make brute force keyboard inputs on numbers.
import logging
import time

import keyboard

WAIT_TIME_SECONDS = 0
TERMINATE_SIGNAL = False


def pad_combo_str(combo: int, digits: int = 6) -> str:
    """ Pad string with 0 characters on left side. """
    s = str(combo)
    s = s.rjust(digits, "0")
    return s


def brute_force_combos(digits: int = 6):
    """ Generator to brute force number range within digits. """
    maximum = pow(10, digits)
    cur = 0
    while cur < maximum:
        yield cur
        cur += 1


def generate_keystrokes(num: int):
    """ Writes keystrokes out to OS input. """
    out = pad_combo_str(num, 6)
    keyboard.write(out)
    keyboard.press('enter')


def loop_combos():
    """ Primary loop to gen and write out combos. """
    start_time = time.time()

    combo_gen = brute_force_combos(6)
    for combo in combo_gen:
        if keyboard.is_pressed('pause'):
            # terminate program if 'end' key is held.
            logging.warning('Terminate signal received. Shutting down.')
            quit()
            break

        logging.debug(f'Attempting combo: {combo}')
        generate_keystrokes(combo)
        time.sleep(WAIT_TIME_SECONDS)

    end_time = time.time()
    diff_time = end_time - start_time
    logging.info(f'generating all combos took: {diff_time} seconds')


def set_hotkeys():
    """ Set trigger rules """
    keyboard.add_hotkey('home', lambda: loop_combos())


# Main execution
if __name__ == '__main__':
    set_hotkeys()
    keyboard.wait()

