from paths.view import View

v = View()
#  v.start()
# v.draw_paths()

x = 100
while(x != -1):
    x = v.switch_cases()
    x = x()

