import cx_Freeze
import cx_Freeze.executable
executaveis = [ 
               cx_Freeze.Executable(script="main.py", icon="img/space.ico") ]
cx_Freeze.setup(
    name = "Space Marker G2",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["img"]
        }
    }, executables = executaveis
)

# Executar CMD
# python setup.py build
# python setup.py bdist_msi