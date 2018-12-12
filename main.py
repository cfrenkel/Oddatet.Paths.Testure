from paths.view import View

# v = View()
#  v.start()
# v.draw_paths()
filters = {
            1: 'paths by time',
            2: 'paths by date and time',
            3: 'paths per location',
            4: 'paths per location and time',
            5: 'paths per location, date and time'
        }
msg = """
            1: paths by time
            2: paths by date and time
            3: paths per location
            4: paths per location and time
            5: paths per location, date and time
        """

inp = input(f'to choose your filter press :{msg}\n ')

if filters.get(inp) is None:
    switch_cases()

print('The result for inp is : ', filters.get(inp))