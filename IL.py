from Data.Generating_algorythms import head_draw_functions as hdf

# Dictionary for the main terminal command options and arguments

diz = {
    # generate
    "triangles" : hdf.DrawTriangle,
    "circles" : hdf.DrawCircle
}

dataset_types = ("training","test")
figures = ("triangles", "circles")
