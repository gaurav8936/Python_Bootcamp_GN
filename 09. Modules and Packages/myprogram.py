# Packages are collections of Modules
# Best practice to create modules for functionality rather than a giant file
# In this example, we are creating a package (this one) and calling the 
## package that we created earlier (mymodule.py) 
# my_func is a function inside mymodule

# from mymodule import my_func

# my_func()

from MyMainPackage import some_main_script

from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()

mysubscript.sub_report()