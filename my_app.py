import tkinter as tk

from music_gui_elements.utility_modules import TriggerToSlew

def main():
    root = tk.Tk()
    root.title('Slew Limiter')

    trigger = TriggerToSlew(
        root,
        #color_background='#ffffff',
        # color_background = 'red',
        # color_foreground = 'white',
        # color_slider_rail = 'white',
        # slider_scale_start = 20,
        # slider_scale_end = 100,
        # height_slider = 400,
        # disable_mult_button = True
    )

    
    root.mainloop()


if __name__ == '__main__':
    main()
    