# Masirah Island Wind Turbine Proposal

# Abstract

Wind-diesel hybrid systems is a power generation scheme that can reduce electricity prices for remote communities that are not connected to a large regional or national grid.  The island of Masirah is a community off the coast of Oman that relies on diesel generators to produce electricity.  Electricity on Masriah is expensive due to the high price of diesel on the island.  The island has a high load in the summer due to air-conditioning, yet also receives high winds during the summer months.  A simulation using Matlab and Homer Energy software was performed for Masirah to determine if wind turbines could be installed to reduce fuel costs.  It was determined that 3 wind turbines could be installed without energy storage, and 8 turbines could be installed with energy storage.  

# Introduction

![map](/png/Figure_7.png)

Remote communities around the world are facing economic and financial challenges due to the high energy prices.  This is typically due to communities not being connected to a large national or regional grid where they would otherwise benefit from cheap and dependable electricity.  This leaves communities facing a difficult situation where they need to overcome geographical, logistical, and economic barriers in order to obtain the required electricity at a reasonable price.  The centralized nature of electricity generation, where large coal, natural gas, and nuclear power plants have typically been the foundation of electrical grids, have left remote communities at a disadvantage.  Centralized power plants are typically located in densely populated areas, whereas remote communities have to find their own solutions to generate electricity.  A typical solution to this dilemma is to install diesel generators that are properly sized to the local electricity demand.  Using diesel generators can mean high fuel costs for operating the generators.  

![wind load profiles](/png/Figure_1.png)

![weibull distribution](/png/Figure_2.png)

One particular community with the potential to utilize the wind-diesel hybrid system is Masirah Island.  Masirah is the largest island of Oman, located about 15 km off the coast of the Arabian Peninsula.  The island is about 15 km long and 5 km wide, with a population of 10,000 people.  Transportation between the mainland and the island consists of ferries and air travel.  The electrical demand is supplied entirely by ten diesel generators ranging in size from 265 to 3136 kW.  Fuel costs for the generators are high due to the costly transportation required to ship the fuel to the island.  The price of diesel on Masirah is typically between $0.4/L and $0.5/L, and a current price of $0.468/L. The electrical demand is highest in the summer due to higher air-conditioning load, while it decreases during the winter months.  The wind speed relatively matches the electrical demand for the island, with wind speeds highest in the summer.  A wind-diesel hybrid system might be an option for this community, and will be evaluated in this simulation.

# Method

For this simulation, one wind turbine will be selected from a list of six Enercon wind turbines to be integrated into a wind-hybrid diesel system on Masirah Island.  The six Enercon turbines to be used in this simulation are shown below.

![candidate wind turbines](/png/Figure_9.png)

The power curves of each wind turbine range from 335 kW to 2.3 MW, and are shown below.

![power curves](/png/Figure_16.png)

Simulations will be performed in Homer Energy along with calculations using Python to determine the optimum turbine and the optimum turbine quantity.  The capital cost, fuel costs, maintenance and operation costs, and generated electricity for eight 1000 MW diesel generators and combinations of different wind turbine quantites will be used as inputs in Homer to calcualte the cost of electricity (COE).  The COE and a concept known as wind penetration will be the criteria to select the optimum quantity and wind turbine.

Wind penetration is defined as the proportion of electricity generated in an electric power system.  A yearly average will be used to calculate the wind penetration, and the equation is shown below.

![wind_penetration_equation](/png/Figure_21.png)

Wind penetration can be used to determine the type of electrical system required to control the wind-diesel hybrid system, and is summarized below.

* Low Wind Penetration (< 20%) - No control system or energy storage required
* Medium Wind Penetration (20%-50%) - A simple control system is needed, but no energy storage is required
* High Wind Penetration (50%-100%) - A complex control system is needed, and energy storage is required

For this simulation, low and medium wind penetration will be evaluated separately, and high wind penetration will not be considered.  Proposals for both low and medium wind penetration situations will be considered.  High wind penetration will not be evaulated because a single simulation involving energy storage in Homer require hours to complete, whereas non-energy storage simulations only need a few seconds.

# Results

The figure below shows the COE results from Homer for each wind-diesel hybrid combination, and the generator only case, which is the current price of electricity on Masiriah.  The results show that any of the candidate wind turbines will reduce the price of electricity, and that there is also an optimum quantity for each wind turbine.  In general, the larger the capacity of the wind turbine, the lower the COE.  

Installing too many turbines could actually be higher than for a smaller number of wind turbines, which shows that too much electricity was generated and had to be curtailed.  Since this simulation did not use energy storage, excess electricity was simply wasted.

The lowest COE for each wind turbine is shown in the graph.  The COE is one of two criteria that will be used to determine the optimum wind turbine candaidate and quantity.  The other criteria being wind penetration, which is shown in the following graph.

![results](/png/Figure_17.png)

Recall that low and medium wind penetration will be considered in this proposal, since they do not require energy storage.  The results are fairly straight forward, with wind penetration increasing linearly with the number of turbines, and higher capacity wind turbines needing fewer turbines to enter the medium and high wind penetration range.  

![results](/png/Figure_18.png)



![low_penetration](/png/Figure_19.png)
![med_penetration](/png/Figure_20.png)

The turbine with the lowest COE ($/kWh) is the Enercon E70, and this will be the chosen turbine for this proposal.  Despite having a lower overall efficiency on Masirah Island, the amount of energy generated when compared to the annualized cost.  Enercon's E44, E48, and E82 were also in consideration for the selected turbine model.  A lower COE value for the E70 will allow it to be more profitable when compared to diesel generation on Masirah, even when diesel is at a lower than average fuel price.

# Conclusion

In order for isolated communities like Masirah to reduce energy costs, it would be recommended to install wind turbines to reduce the expensive fuel cost needed to operate diesel generators.  It was determined that without energy storage, 3 turbines could be installed to reduce the fuel costs.  This was determined because 3 wind turbines do not produce excess electricity on Masirah.  For the simulation with energy storage, it was determined that 8 turbines could be used.  This number was determined from comparing the COE of wind turbines with batteries and the COE of diesel generators at the price of diesel on Masirah.  More turbine may be able to be installed on Masirah without energy storage if a dump load is used to divert excess electricity generated during high winds and a low load.  This simulation shows that isolated communities that are not connected to a regional or national grid could utilize wind turbines to reduce electricity costs.  The addition of wind turbines for remote communities not only reduces electricity prices, but also emits fewer greenhouse gases and gives these communities a sense of energy independence.  
