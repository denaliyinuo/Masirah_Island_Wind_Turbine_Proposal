# Masirah Island Wind Turbine Proposal

# Abstract

Wind-diesel hybrid systems are a power generation scheme that can reduce electricity prices for remote communities that are not connected to a large regional or national grid. Masirah Island is a community off the coast of Oman that relies on diesel generators to produce electricity. Electricity on Masirah is expensive due to the high price of diesel on the island.  The island has a high load in the summer due to air-conditioning, yet also receives high winds during the summer months.  A simulation using Matlab and Homer Energy software was performed for Masirah to determine if wind turbines could be installed to reduce fuel costs and the cost of electricity (COE). Three proposals were put forward to reduce diesel consumption and the price of electricity. The COE could be reduced by approximately 3¢ to 6¢ per kWh, with a break-even time for the wind turbine investment of approximately five to seven years, and a reduction in annual fuel consumption of between 15% and 30%.


# Introduction

Remote communities around the world are facing economic and financial challenges due to the high energy prices. This is typically due to communities not being connected to a large national or regional grid where they would otherwise benefit from cheap and dependable electricity. This leaves communities facing a difficult situation where they need to overcome geographical, logistical, and economic barriers in order to obtain the required electricity at a reasonable price. The centralized nature of electricity generation, where large coal, natural gas, and nuclear power plants have typically been the foundation of electrical grids, have left remote communities at a disadvantage. Centralized power plants are typically located in densely populated areas, whereas remote communities have to find their own solutions to generate electricity. A typical solution to this dilemma is to install diesel generators that are properly sized to the local electricity demand. Using diesel generators can mean high fuel costs for operating the generators.

![map](/png/Figure_7.png)
Figure 1: Map of Oman and Masirah Island

One particular community with the potential to utilize the wind-diesel hybrid system is Masirah Island. Masirah is the largest island of Oman, located about 15 km off the coast of the Arabian Peninsula. The island is about 15 km long and 5 km wide, with a population of 10,000 people. Transportation between the mainland and the island consists of ferries and air travel. The electrical demand is supplied entirely by ten diesel generators ranging in size from 265 to 3136 kW. Fuel costs for the generators are high due to the costly transportation required to ship the fuel to the island. The price of diesel on Masirah is typically between $0.4/L and $0.6/L, and a price of $0.468/L as of February 2021. The electrical demand is highest in the summer due to higher air-conditioning load, while it decreases during the winter months. The wind speed relatively matches the electrical demand for the island, with wind speeds highest in the summer. A wind-diesel hybrid system might be an option for this community, and will be evaluated in this simulation.

The wind and load profiles are shown in figure 2, and will be used to calculate the potential electrical production from wind energy, as well as the quantity of wind turbines that can be installed. The number of turbines will be influenced by electrical demand, the diesel generator electrical generation, the wind speed, the power curve of the wind turbine, and the whether or not there is a control system.

![wind load profiles](/png/Figure_28.png)
Figure 2: Load and wind speed profiles of Masirah Island

The Weibull distribution is shown is graph 3, which is a great approximation for the wind speed distribution of a particular location. This distribution, along with the power curve of a wind turbine, can be used to calculate the electricity generation by a wind turbine. The value of k equals 1.38, which means that Masirah has a large distribution in wind speeds. The value of c is 5.34, which is approximately equal to the average wind speed on Masirah.

![weibull distribution](/png/Figure_2.png)
Figure 3: Weibull distribution of one-years’ worth of wind speeds on Masirah Island

# Method

For this simulation, one wind turbine will be selected from a list of six Enercon wind turbines to be integrated into a wind-hybrid diesel system on Masirah Island, and the cost of electricity (COE) will be calculated, and will be compared to the current COE. The six Enercon turbines to be used in this simulation are shown in figure 4.

![candidate wind turbines](/png/Figure_9.png)

The power curves of each wind turbine are shown in figure 5. The capacities range from 335 kW to 2.3 MW, and also differ in their abilities to extract more energy at lower wind speeds. An example of this is the E-53 model possessing a better ability of generating more power at low wind speeds than the E-48 and E-44 models, even though the latter two models have either the same or higher rated capacity.

![power curves](/png/Figure_26.png)
Figure 5: Power curves of the six Enercon candidate wind turbines

Simulations will be performed in Homer Energy along with calculations using Python to determine the optimum turbine and the optimum turbine quantity. The capital cost, fuel costs, maintenance and operation costs, and generated electricity for eight 1000 MW diesel generators and combinations of different wind turbine quantities will be used as inputs in Homer to calculate the cost of electricity (COE). The COE and a concept known as wind penetration will be the criteria to select the optimum quantity and wind turbine.

Wind penetration is defined as the proportion of electricity generated in an electric power system. A yearly average will be used to calculate the wind penetration, and the equation is shown below.

![wind_penetration_equation](/png/Figure_21.png)

Wind penetration can be used to determine the type of electrical system required to control the wind-diesel hybrid system, and is summarized below. Wind penetration for wind-diesel hybrid systems can be separated between three levels of low, medium and high wind penetration, and each level requires a different system for controlling the wind turbines and integrating them into an electrical grid.


# Results

Figure 6 shows the COE results from Homer for each wind-diesel hybrid combination, and the generator only case, which is the current price of electricity on Masirah. The results show that any of the candidate wind turbines will reduce the price of electricity, and that there is also an optimum quantity for each wind turbine. In general, the larger the capacity of the wind turbine, the lower the COE.  

Installing too many turbines could actually cause a higher COE than for a smaller number of wind turbines, which shows that wind farm had to be curtailed. Since this simulation did not use energy storage, excess electricity was simply wasted.

The lowest COE for each wind turbine is shown in the graph. The COE is one of two criteria that will be used to determine the optimum wind turbine candidate and quantity. The other criteria being wind penetration, which is shown in figure 7.

![results](/png/Figure_17.png)
Figure 6: Wind-hybrid COE for each wind turbine and different wind turbine quantities ranging from one to 20

Recall that low and medium wind penetration will be considered in this proposal, since they do not require energy storage.  The results in figure 7 are fairly straight forward, with wind penetration increasing linearly with the number of turbines, and higher capacity wind turbines needing fewer turbines to enter the medium and high wind penetration range.

![results](/png/Figure_18.png)
Figure 7: Wind penetration for each wind turbine at different quantities ranging from one to 20

The results in table 1 show the quantity of each wind turbine at the lowest COE within the low wind penetration range. All six wind turbines have a COE in the $0.27 to $0.28/kWh range. Three E-53 wind turbines model have the lowest COE, and this combination will be submitted as the low wind penetration proposal. Not only does the E-53 model have the lowest COE, it also has a high efficiency on Masirah, most likely due to its ability to extract energy from the wind at low speeds.

![low_penetration](/png/Figure_19.png)

For medium wind penetration, the wind-hybrid system is required. The results show a lower COE for each wind turbine model, with three E-82 turbines having the lowest COE. One issue with the E-82 turbine is the sheer size of the blades and tower, which could be an issue with transportation and installation on such a small and remote community. Therefore, the E-82 and the E-53, which has the second lowest COE, will be proposed for the medium wind penetration range.

![med_penetration](/png/Figure_20.png)

Figure 8 shows the investment break-even time for the three proposals. The break-even time for this calculation is defined as the amount of time it will take for the savings in fuel costs to equal the initial capital investment of the wind turbines. The maintenance and operation costs were excluded for this calculation. Since the typical cost of diesel fuel on Masirah ranges from $0.4 to $0.6 per liter, a price of $0.5/L was used to calculate the break-even time. The proposals of three E-53 turbines and three E-82 turbines have a break-even time of 5.3 and 5.8 years, respectively. The proposal of eight E-53 turbines has a break-even time of 7.3 years.

# Conclusion

In order for isolated communities like Masirah to reduce energy costs, it would be recommended to install wind turbines to reduce the expensive fuel cost needed to operate diesel generators. The best proposal was concluded to install three E-82 turbines, with the lowest COE, a relatively low 5.8 year break-even time period, and resulting in a 28% reduction in fuel consumption. If transportation and installation of the E-82 model proves difficult, a secondary plan of E-53 wind turbines could be installed.

It was determined for the low wind penetration range, three E-53 wind turbines would result in the lowest COE of $0.271/kWh, and a break-even time period of 7.3 years. For the medium wind penetration range, three E-82 wind turbines with a COE of $0.243/kWh could be installed and a break-even time period of 5.8 years. 

This simulation shows that isolated communities that are not connected to a regional or national grid could utilize wind turbines to reduce electricity costs. The addition of wind turbines for remote communities not only reduces electricity prices, but also emits fewer greenhouse gases and gives these communities a sense of energy independence.
