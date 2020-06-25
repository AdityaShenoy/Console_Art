import curses
from PIL import Image

def main(scr):
  console_height, console_width = scr.getmaxyx()

  img = Image.open('F:\\github\\Console_Art\\binary.png')
  img_height, img_width = img.height, img.width

  img = img.resize((console_height * img_width // img_height, console_height))

  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

  pixels = img.load()
  for y in range(img.height):
    for x in range(img.width):
      scr.attron(curses.color_pair(pixels[x, y][0] // 255 + 1))
      scr.addstr(y, (console_width - img.width) // 2 + x, ' ')
      scr.attroff(curses.color_pair(pixels[x, y][0] // 255 + 1))
  scr.refresh()
  scr.getch()

curses.wrapper(main)