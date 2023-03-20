# OnionBench
![OnionBench](logo.png)
# Get started
* Clone the project files:
`git clone https://github.com/z3ven/OnionBench/`
* Go to the project folder: `cd OnionBench-main`
* Install requirements: `pip install -r requirements.txt`
# Usage
All the commands are executing via `python bench.py <testname> <times>`
## Commands
*  `cpu <times>`: Measures which time does your c.p.u spend to make division. Example: 
`python bench.py cpu 100000`. The normal number of times is 10000-1000000. Normal speed on 10000 is between 0.10-0.99 seconds(Tested on M1 macbook air)![image](https://user-images.githubusercontent.com/91781891/226451102-4ade247c-6b22-481c-9004-0badd08e1950.png)

* `network <times>`: The normal number of times is 1-100. Normal speed on 10 is between 1-10 seconds. It may depend on your internet. Example:
`python bench.py network 10`.
* `gpu <times>`: The same test as cpu, but using gpu cores.
* `disk <times>`: Measures how fast is your disk.
* `mrproper`: Cleares bound_cache folder
# Other details
* On some computers gpu could work slower than cpu.
* Please do not write 100000000000 times in disk command if you dont wont to break your ssd.
* Sometimes network test could break. It often causes when there is some problems with network card, or internet.
