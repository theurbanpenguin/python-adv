import subprocess
# Specify the package you want to install
package_name = "numpy"
def display_numpy_version():
    import numpy as np
    return np.__version__


if __name__ == '__main__':

    # Use pip to install the package
    try:
        subprocess.check_call(["pip", "install", package_name])
        print(f"Successfully installed {package_name}")
        print(f"Numpy Version = {display_numpy_version()}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}")
