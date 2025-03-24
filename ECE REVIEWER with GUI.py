import tkinter as tk
import random


class Reviewer:
    exam_sheet = {
    "one": ["The name of pure semiconductor material that has an equal number of electrons and holes",  #question
            "C. intrinsic", #answer
            "A. n-type", #choice1
            "B. pure type", #choice2
            "C. intrinsic", #choice3
            "D. p-type"], #choice4

    "two": ["Elements that have four valence electrons are classified as",
            "C. elemental semiconductor",
            "A. conductor",
            "B. insulator",
            "C. elemental semiconductor",
            "D. compound semiconductor"],

    "three": ["An example of an elemental semiconductor.",
              "A. Germanium (Ge)", 
              "A. Germanium (Ge)", 
              "B. Gallium Arsenide (GaAs)", 
              "C. Gallium Phosphide (GaP)", 
              "D. Aluminum Arsenide (AlAs)"],

    "four": ["Which of the following is an example of a compound semiconductor?", 
             "D. All of the above", 
             "A. Gallium Arsenide (GaAs)", 
             "B. Gallium Phosphide (GaP)", 
             "C. Aluminum Arsenide (AlAs)", 
             "D. All of the above"],

    "five": ["Germanium has an atomic number of 32 and an atomic weight of approximately 72 amu. How many electrons, protons, and neutrons are there?",
             "A. 32, 32, 40",
             "A. 32, 32, 40",
             "B. 32, 32, 104",
             "C. 40, 32, 32",
             "D. 40, 32, 104"],

    "six": ["The chemical bond that is present in a crystal lattice of silicon atoms.",
            "A. covalent bond",
            "A. covalent bond",
            "B. electrovalent bond",
            "C. ionic bond",
            "D. metallic bond"],

    "seven": ["The atomic weight of a silicon atom is approximately 28 amu. How many electrons, protons, and neutrons does the atom consist?",
              "B. 14, 14, 42",
              "A. 14, 42, 14",
              "B. 14, 14, 42",
              "C. 42, 14, 14",
              "D. 14, 14, 14"],

    "eight": ["What is the total charge at the nucleus of a silicon atom?",
              "D. 14e C",
              "A. -12e C",
              "B. 12e C",
              "C. -14e C",
              "D. 14e C"],

    "nine": ["In materials, what do you call the area that separates the valence band and the conduction band?",
             "D. A and B are correct",
             "A. energy gap",
             "B. forbidden band",
             "C. insulation band",
             "D. A and B are correct"],

    "ten": ["At absolute zero temperature, a semiconductor acts as",
            "A. an insulator",
            "A. an insulator",
            "B. a conductor",
            "C. a semi-insulator",
            "D. usual"],

    "eleven": ["The electron flow in a semiconductor material is",
               "A. opposite in direction of hole flow",
               "A. opposite in direction of hole flow",
               "B. the same direction with hole flow",
               "C. the drift current",
               "D. known as the conventional current"],
    
    "twelve": ["Typical range of the resistivity of a semiconductor",
               "B. 10⁻⁵ - 10⁻⁸ Ω-cm",
               "A. 10⁻¹⁵ - 10⁻¹⁸ Ω-cm",
               "B. 10⁻⁵ - 10⁻⁸ Ω-cm",
               "C. 10 - 10⁴ Ω-cm",
               "D. 10⁸ - 10¹⁵ Ω-cm"],

    "thirteen": ["Chemical bond that is significant in metals",
                 "D. metallic bonding",
                 "A. ionic bonding",
                 "B. electrovalent bonding",
                 "C. covalent bonding",
                 "D. metallic bonding"],

    "fourteen": ["A semiconductor that is free from impurities",
                 "A. intrinsic semiconductor",
                 "A. intrinsic semiconductor",
                 "B. extrinsic semiconductor",
                 "C. compensated semiconductor",
                 "D. elemental semiconductor"],

    "fifteen": ["The process of adding impurities in a semiconductor material.",
                "C. doping",
                "A. growing",
                "B. diffusion",
                "C. doping",
                "D. depleting"],

    "sixteen": ["Impurities with five valence electrons.",
                "B. donor",
                "A. acceptor",
                "B. donor",
                "C. trivalent",
                "D. pentavalent"],

    "seventeen": ["Example of acceptor impurities.",
                  "B. trivalent impurities",
                  "A. pentavalent impurities",
                  "B. trivalent impurities",
                  "C. tetravalent impurities",
                  "D. hexavalent impurities"],
    
    "eighteen": ["If the substance used in doping has less than four valence electrons, it is known as",
                 "A. acceptor",
                 "A. acceptor",
                 "B. donor",
                 "C. trivalent",
                 "D. pentavalent"],

    "nineteen": ["Commonly used as donor impurities.",
                 "D. all of the above",
                 "A. Antimony(Sb)",
                 "B. Arsenic(As)",
                 "C. Phosphorus(P)",
                 "D. all of the above"],

    "twenty": ["Example of trivalent impurities.",
               "D. all of the above",
               "A. Boron(B)",
               "B. Gallium(Ga)",
               "C. Indium(In)",
               "D. all of the above"],

    "twenty_one": ["Donor-doped semiconductor becomes a",
                   "A. N-type semiconductor",
                   "A. N-type semiconductor",
                   "B. good conductor",
                   "C. p-n semiconductor",
                   "D. P-type semiconductor"],

    "twenty_two": ["What do you call a semiconductor that is doped with both donor and acceptor impurities?",
                   "B. compensated semiconductor",
                   "A. double doped semiconductor",
                   "B. compensated semiconductor",
                   "C. compound semiconductor",
                   "D. diffused semiconductor"],

    "twenty_three": ["The resistance of a semiconductor is known as",
                     "A. bulk resistance",
                     "A. bulk resistance",
                     "B. intrinsic resistance",
                     "C. extrinsic resistance",
                     "D. dynamic resistance"],

    "twenty_four": ["The most extensively used semiconductor.",
                    "A. silicon",
                    "A. silicon",
                    "B. germanium",
                    "C. gallium phosphide",
                    "D. gallium arsenide"],

    "twenty_five": ["Semiconductor whose electron and hole concentrations are equal.",
                    "B. intrinsic semiconductor",
                    "A. extrinsic semiconductor",
                    "B. intrinsic semiconductor",
                    "C. compensated semiconductor",
                    "D. doped semiconductor"],

    "twenty_six": ["Silicon is widely used over germanium due to its several advantages, what do you think is its most significant advantage?",
                   "D. low leakage current",
                   "A. abundant",
                   "B. cheap",
                   "C. temperature stable",
                   "D. low leakage current"],

    "twenty_seven": ["Current flow in a semiconductor that is due to the applied electric field.",
                     "D. drift current",
                     "A. diffusion current",
                     "B. conventional current",
                     "C. drift velocity",
                     "D. drift current"],

    "twenty_eight": ["The movement of charge carriers in a semiconductor even without the application of electric potential.",
                     "A. diffusion current",
                     "A. diffusion current",
                     "B. conventional current",
                     "C. drift current",
                     "D. saturation current"],

    "twenty_nine": ["Typically, how much energy is required for a valence electron to move to the conduction band for a doped semiconductor?",
                    "B. 0.05 eV",
                    "A. 0 eV",
                    "B. 0.05 eV",
                    "C. 1.0 eV",
                    "D. 5.0 eV"],

    "thirty": ["Conduction of electrons in a doped semiconductor happens at",
               "A. conduction band",
               "A. conduction band",
               "B. forbidden band",
               "C. valence band",
               "D. nuclei band"],

    "thirty_one": ["Theoretically, where does the conduction of holes occur in a doped semiconductor?",
                   "C. valence band",
                   "A. conduction band",
                   "B. forbidden band",
                   "C. valence band",
                   "D. empty band"],

    "thirty_two": ["In energy band diagram of a doped semiconductor, the donor level",
                   "B. is near the conduction band",
                   "A. is near the valence band",
                   "B. is near the conduction band",
                   "C. is exactly in between the valence and conduction band",
                   "D. depends on the amount of doping"],

    "thirty_three": ["The acceptor level in a doped semiconductor",
                     "A. is near the valence band level",
                     "A. is near the valence band level",
                     "B. is near the conduction level",
                     "C. is exactly in between the conduction and valence band",
                     "D. will depend on the concentration of doping"],

    "thirty_four": ["In a semiconductor material, what will happen to the number of free electrons when the temperature rises?",
                    "A. increases",
                    "A. increases",
                    "B. decreases exponentially",
                    "C. decreases",
                    "D. remains the same"],

    "thirty_five": ["The electrical resistance of a semiconductor material will _____ as the temperature increases.",
                    "C. decrease",
                    "A. increase",
                    "B. increase exponentially",
                    "C. decrease",
                    "D. not change"],

    "thirty_six": ["The potential required to remove a valence electron",
                   "D. ionization potential",
                   "A. valence potential",
                   "B. threshold potential",
                   "C. critical potential",
                   "D. ionization potential"],

    "thirty_seven": ["Among the given elements, which is considered as nonmetal?",
                      "A. silicon (Si)",
                      "A. silicon (Si)",
                      "B. germanium (Ge)",
                      "C. tin (Sn)",
                      "D. lead (Pb)"],

    "thirty_eight": ["A semiconductor that is classified as a metalloid or semimetal",
                      "B. germanium (Ge)",
                      "A. silicon (Si)",
                      "B. germanium (Ge)",
                      "C. tin (Sn)",
                      "D. carbon (C)"],

    "thirty_nine": ["Semiconductor that is very rare, it only occurs in minute quantities in many metal sulfides",
                     "B. germanium (Ge)",
                     "A. silicon (Si)",
                     "B. germanium (Ge)",
                     "C. tin (Sn)",
                     "D. lead (Pb)"],

    "forty": ["Compound semiconductors are also known as",
              "D. inter-metallic semiconductors",
              "A. compensated semiconductors",
              "B. amorphous semiconductors",
              "C. organic semiconductors",
              "D. inter-metallic semiconductors"],

    "forty_one": ["What semiconductor that is mostly used in devices requiring the emission or absorption of lights?",
                  "C. compound semiconductor",
                  "A. amorphous semiconductor",
                  "B. organic semiconductor",
                  "C. compound semiconductor",
                  "D. elemental semiconductor"],

    "forty_two": ["For high-speed integrated circuits, which semiconductor material given below is best to be used?",
                  "D. gallium arsenide",
                  "A. silicon",
                  "B. germanium",
                  "C. carbon",
                  "D. gallium arsenide"],

    "forty_three": ["How much impurity concentration is needed for a sample of silicon to change its electrical property from a poor conductor to a good conductor?",
                    "C. one part per million",
                    "A. one part per hundred",
                    "B. one part per thousand",
                    "C. one part per million",
                    "D. one part per billion"],

    "forty_four": ["The restriction of certain discrete energy levels in a semiconductor material can be predicted generally by using what model?",
                   "A. Bohr model",
                   "A. Bohr model",
                   "B. string model",
                   "C. wave model",
                   "D. particle model"],

    "forty_five": ["Is defined as the energy acquired by an electron moving through a potential of one volt.",
                   "D. electron Volt (eV)",
                   "A. electron Joules (eJ)",
                   "B. electron-potential",
                   "C. oxidation potential",
                   "D. electron Volt (eV)"],

    "forty_six": ["At room temperature, in a perfect silicon crystal, the equilibrium concentration of thermally generated electrons in the conduction band is about",
                  "B. 1.5 × 10¹⁰ per cubic cm.",
                  "A. 1.5 × 10⁵ per cubic cm.",
                  "B. 1.5 × 10¹⁰ per cubic cm.",
                  "C. 1.5 × 10¹⁵ per cubic cm.",
                  "D. 1.5 × 10²⁰ per cubic cm."],

    "forty_seven": ["What is the basis in operation of semiconductor photoconductors?",
                    "D. EHP optical generation",
                    "A. EHP generation",
                    "B. EHP degeneration",
                    "C. EHP optical degeneration",
                    "D. EHP optical generation"],

    "forty_eight": ["The semiconductor that is used in xerography",
                    "A. selenium (Se)",
                    "A. selenium (Se)",
                    "B. gallium phosphide (GaP)",
                    "C. cadmium compound",
                    "D. photoconductive material"],

    "forty_nine": ["A silicon material has an intrinsic concentration ni = 10¹⁰ per cubic centimeter at room temperature. If it is doped with 10¹⁵ antimony atoms per cubic centimeter, what is now the approximate electron concentration at the conduction band?",
                   "C. 10¹⁵ electrons",
                   "A. 10⁵ electrons",
                   "B. 10¹⁰ electrons",
                   "C. 10¹⁵ electrons",
                   "D. 10²⁰ electrons"],

    "fifty": ["When an electron at the conduction band falls back to the valence band it will recombine with the hole. This is known as",
              "D. recombination",
              "A. regeneration",
              "B. reunion",
              "C. combination",
              "D. recombination"],

    "fifty_one": ["Which semiconductor is mostly used to detect near-infrared?",
                  "B. germanium",
                  "A. silicon",
                  "B. germanium",
                  "C. carbon",
                  "D. silicon carbide"],

    "fifty_two": ["What semiconductor that is good for high-temperature applications?",
                  "C. silicon carbide (SiC)",
                  "A. indium antimonide (InSb)",
                  "B. gallium antimonide (GaSb)",
                  "C. silicon carbide (SiC)",
                  "D. diamond (C)"],

    "fifty_three": ["Among the given semiconductors below, which has the highest mobility?",
                    "D. indium antimonide",
                    "A. silicon",
                    "B. germanium",
                    "C. gallium arsenide",
                    "D. indium antimonide"],

    "fifty_four": ["A semiconducting glass is known as",
                   "B. amorphous semiconductor",
                   "A. isomorphous semiconductor",
                   "B. amorphous semiconductor",
                   "C. organic semiconductor",
                   "D. compound semiconductor"],

    "fifty_five": ["For an electroluminescent of green and red lights, which semiconductor is best?",
                   "D. gallium phosphide",
                   "A. silicon carbide",
                   "B. gallium arsenide",
                   "C. indium antimonide",
                   "D. gallium phosphide"],

    "fifty_six": ["Typical range of power dissipation for a semiconductor to be considered as 'low power' or 'small signal'.",
                  "A. less than 1 watt",
                  "A. less than 1 watt",
                  "B. 5 < P < 10 watts",
                  "C. 10 < P < 20 watts",
                  "D. 20 watts above"],

    "fifty_seven": ["In the design of high-power semiconductor devices, it involves what factors?",
                    "D. all of the above",
                    "A. making the size of the semiconductor bigger",
                    "B. packing the device into a bigger case",
                    "C. excellent contact between the semiconductor and the case",
                    "D. all of the above"],

    "fifty_eight": ["How to have a better high-frequency response in designing semiconductor devices?",
                    "D. all of the above",
                    "A. make the chip as small as possible",
                    "B. the leads should be made shorter and smaller",
                    "C. smaller packaging",
                    "D. all of the above"],

    "fifty_nine": ["Before an electron can participate in the conduction of electricity, it must leave from the valence band and transfer to the conduction band. Transferring to the conduction band involves energy acquisition by an electron from external sources and this energy must be greater than the energy gap of the material. Which semiconductor material has the highest energy gap?",
                    "A. Zinc Sulfide (ZnS)",
                    "A. Zinc Sulfide (ZnS)",
                    "B. silicon (Si)",
                    "C. germanium (Ge)",
                    "D. Indium Antimonide (InSb)"],

    "sixty": ["Which of the following semiconductors has the smallest energy gap?",
              "D. InSb",
              "A. ZnS",
              "B. Si",
              "C. Ge",
              "D. InSb"],

    "sixty_one": ["The ease with which a charge carrier (electron or hole) moves in a semiconductor material is known as mobility. It is also defined as the average drift velocity of electrons and holes per unit electrostatic field. Which of the semiconductor materials has the highest value of electron-mobility?",
                  "A. InSb",
                  "A. InSb",
                  "B. Ge",
                  "C. Si",
                  "D. AlP"],

    "sixty_two": ["In semiconductor materials, electrons have a higher value of mobility than holes, but which semiconductor material has the slowest electron-mobility?",
                  "D. AlP",
                  "A. InSb",
                  "B. GaP",
                  "C. GaAs",
                  "D. AlP"],

    "sixty_three": ["Solar cell is a semiconductor electric-junction device, which absorbs the radiant energy of sunlight and converts it directly and efficiently into electrical energy. This device, uses what type of semiconductor materials?",
                    "D. all of the above",
                    "A. single-crystal silicon",
                    "B. amorphous or polycrystalline silicon",
                    "C. GaAs, CdS, CdTe, CuS",
                    "D. all of the above"],

    "sixty_four": ["What is formed when n-type and p-type semiconductors are brought together?",
                   "A. pn junction",
                   "A. pn junction",
                   "B. semiconductor junction",
                   "C. energy band gap",
                   "D. semiconductor diode"],

    "sixty_five": ["PN junction acts as a one-way valve for electrons because ________.",
                   "D. when electrons are pumped from P to N, free electrons and holes are forced apart leaving no way for electrons to cross the junction",
                   "A. the circuit in which the diode is used, only attempts to pump electrons in one diode",
                   "B. electrons tend to follow the direction of the hole",
                   "C. there is a little mechanical switch inside a diode",
                   "D. when electrons are pumped from P to N, free electrons and holes are forced apart leaving no way for electrons to cross the junction"],

    "sixty_six": ["The device that is formed when an n-type and p-type semiconductors are brought together.",
                  "D. junction diode",
                  "A. pn junction",
                  "B. semiconductor junction",
                  "C. depletion region",
                  "D. junction diode"],

    "sixty_seven": ["An external voltage applied to a junction reduces its barrier and aids current to flow through the junction.",
                    "D. forward bias",
                    "A. reverse bias",
                    "B. external bias",
                    "C. junction bias",
                    "D. forward bias"],

    "sixty_eight": ["A device containing an anode and a cathode or a pn junction of a semiconductor as the principal elements and provides unidirectional conduction.",
                    "A. diode",
                    "A. diode",
                    "B. diac",
                    "C. triode",
                    "D. triac"],

    "sixty_nine": ["Unidirectional conduction in two-electrodes in any device other than a diode, such that rectification between the grid and cathode of a triode, or asymmetrical conduction between the collector and base of a transistor is called ________.",
                   "B. diode action",
                   "A. rectification",
                   "B. diode action",
                   "C. clipping",
                   "D. clamping"],

    "seventy": ["The p-type material in a semiconductor junction diode is technically termed as",
                "D. anode",
                "A. positive terminal",
                "B. negative terminal",
                "C. cathode",
                "D. anode"],

    "seventy_one": ["Cathode in a semiconductor junction diode is referred to the",
                    "D. n-type terminal",
                    "A. positive terminal",
                    "B. junction",
                    "C. p-type terminal",
                    "D. n-type terminal"],

    "seventy_two": ["The area in the semiconductor diode where there are no charge carriers",
                    "B. depletion region",
                    "A. depletion layer",
                    "B. depletion region",
                    "C. depletion mode",
                    "D. depletion area"],

    "seventy_three": ["Depletion region is an area in a semiconductor device where there are no charge carriers exist. This will be always near the junction of n-type and p-type materials. What causes this junction to be depleted by charge carriers?",
                      "D. Due to the combination of positively charged holes and negatively charged electrons",
                      "A. Due to the recombination of holes and electrons at the junction",
                      "B. Due to the cancellation of positively charged protons and negatively charged electrons",
                      "C. Due to the annihilation of charge carriers",
                      "D. Due to the combination of positively charged holes and negatively charged electrons"],

    "seventy_four": ["A junction diode is said to be forward-biased if",
                     "A. Anode is supplied more positive than the cathode.",
                     "A. Anode is supplied more positive than the cathode.",
                     "B. Anode is supplied more negative than the cathode.",
                     "C. A voltage greater than threshold is applied, with cathode less positive than anode.",
                     "D. A voltage greater than threshold is applied, with cathode less negative than anode."],

    "seventy_five": ["What do you call the very small amount of current that will flow in the diode when it is reverse biased?",
                     "B. reverse saturation current",
                     "A. saturation current",
                     "B. reverse saturation current",
                     "C. cut-off current",
                     "D. holding current"],

    "seventy_six": ["When the diode is supplied with a forward direction potential but with a magnitude less than the threshold voltage of the diode, still it will not 'turn-on' and will only allow a very small amount of current to pass. This very small current is known",
                    "D. as cut-off current",
                    "A. as leakage current",
                    "B. as forward saturation current",
                    "C. as holding current",
                    "D. as cut-off current"],

    "seventy_seven": ["The minimum voltage required before a diode can totally conduct in a forward direction.",
                      "D. threshold voltage",
                      "A. triggering voltage",
                      "B. breakdown voltage",
                      "C. saturation voltage",
                      "D. threshold voltage"],

    "seventy_eight": ["What will happen to the threshold voltage of the diode when it operates at higher temperatures?",
                       "C. decreases",
                       "A. increases",
                       "B. increases exponentially",
                       "C. decreases",
                       "D. decreases exponentially"],

    "seventy_nine": ["The forward current in a conducting diode will ________ as the operating temperature increases.",
                     "D. increase",
                     "A. not be affected",
                     "B. decrease",
                     "C. decrease exponentially",
                     "D. increase"],

    "eighty": ["As the operating temperature of a reverse-biased diode is increased, its leakage or reverse saturation current will ________.",
               "B. increase exponentially",
               "A. increase",
               "B. increase exponentially",
               "C. decrease",
               "D. decrease exponentially"],

    "eighty_one": ["The small value of direct current that flows when a semiconductor device has reverse bias.",
                   "C. reverse current",
                   "A. surge current",
                   "B. bias current",
                   "C. reverse current",
                   "D. current limit"],

    "eighty_two": ["Normally, diodes will not conduct when reverse-biased, but if the reverse voltage is increased further, a point will be reached where the diode gives up and allows the current to surge. This voltage is one of the limiting parameters of diodes and is known as",
                   "D. all are correct",
                   "A. breakdown voltage (V_BR)",
                   "B. peak inverse voltage (PIV)",
                   "C. peak reverse voltage (PRV)",
                   "D. all are correct"],

    "eighty_three": ["For a silicon diode, calculate the current at room temperature if the forward voltage, V_F = 0.3 V and the reverse saturation current I_S = 100 nA.",
                     "A. 32.8 µA",
                     "A. 32.8 µA",
                     "B. 10.8 µA",
                     "C. 32.8 mA",
                     "D. 10.8 mA"],

    "eighty_four": ["The breakdown voltage of a junction diode will ________.",
                    "C. decrease as operating temperature rises.",
                    "A. increase as operating temperature rises.",
                    "B. increase exponentially as operating temperature rises.",
                    "C. decrease as operating temperature rises.",
                    "D. not change as operating temperature rises."],

    "eighty_five": ["Calculate the new threshold voltage of a germanium diode when it operates at 100°C.",
                    "A. 0.113 V",
                    "A. 0.113 V",
                    "B. 0.188 V",
                    "C. 0.215 V",
                    "D. 0.513 V"],

    "eighty_six": ["A silicon diode has a reverse saturation current of 50 nA at room temperature. If the operating temperature is raised by 50°C, what is now the reverse saturation current?",
                   "D. 1.66 µA",
                   "A. 105.56 nA",
                   "B. 287.73 nA",
                   "C. 827.89 nA",
                   "D. 1.66 µA"],

    "eighty_seven": ["In every increase of 10°C in the operating temperature of a diode will cause its reverse saturation current to",
                     "B. double",
                     "A. decrease",
                     "B. double",
                     "C. triple",
                     "D. quadruple"],

    "eighty_eight": ["What do you call the resistance of the diode when operating at a steady state voltage?",
                     "A. dc resistance",
                     "A. dc resistance",
                     "B. dynamic resistance",
                     "C. ac resistance",
                     "D. average resistance"],

    "eighty_nine": ["The resistance of the diode that is significant when operating with a small ac signal.",
                    "C. dynamic resistance",
                    "A. dc resistance",
                    "B. static resistance",
                    "C. dynamic resistance",
                    "D. average resistance"],

    "ninety": ["When a diode is used in large ac voltages, the resistance that is to be considered is",
               "D. average resistance",
               "A. dc resistance",
               "B. static resistance",
               "C. dynamic resistance",
               "D. average resistance"],

    "ninety_one": ["At forward bias condition, what will happen to the diode resistance when the applied voltage is increased?",
                   "C. will decrease",
                   "A. will also increase",
                   "B. will increase exponentially",
                   "C. will decrease",
                   "D. will not change"],

    "ninety_two": ["The primary use of Zener diode in electronic circuits.",
                   "C. voltage regulator",
                   "A. resistance regulator",
                   "B. rectifier",
                   "C. voltage regulator",
                   "D. current regulator"],

    "ninety_three": ["What phenomenon in electronics does an avalanche breakdown primarily depend on?",
                     "C. Ionization",
                     "A. Doping",
                     "B. Recombination",
                     "C. Ionization",
                     "D. Collision"],

    "ninety_four": ["When a diode is reverse biased the depletion region widens, since it is in between positively charged holes and negatively charged electrons, it will have an effect of a capacitor, this capacitance is called what?",
                    "D. transition capacitance",
                    "A. diffusion capacitance",
                    "B. storage capacitance",
                    "C. stray capacitance",
                    "D. transition capacitance"],

    "ninety_five": ["In a semiconductor diode, the total capacitance, that is the capacitance between terminals and electrodes, and the internal voltage variable capacitance of the junction is called",
                    "D. diode capacitance",
                    "A. diffusion capacitance",
                    "B. transition capacitance",
                    "C. depletion-region capacitance",
                    "D. diode capacitance"],

    "ninety_six": ["What capacitance is significant when the diode is forward biased?",
                   "A. diffusion capacitance or storage capacitance",
                   "A. diffusion capacitance or storage capacitance",
                   "B. transition capacitance",
                   "C. depletion-region capacitance",
                   "D. stray capacitance"],               
                                                         
}


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ECE Reviewer Quiz")
        self.root.geometry("600x400")
        self.reviewer = Reviewer()
        self.question_id = None

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=500, justify="left")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), width=50, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.feedback_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        self.feedback_label.config(text="", fg="black")
        self.question_id = random.choice(list(self.reviewer.exam_sheet.keys()))
        data = self.reviewer.exam_sheet[self.question_id]

        self.correct_letter = data[1][0]  
        self.correct_answer = data[1]

        self.question_label.config(text=data[0])
        for i in range(4):
            self.option_buttons[i].config(text=data[i + 2], state="normal")

    def check_answer(self, idx):
        selected_letter = self.option_buttons[idx]['text'][0]

        if selected_letter == self.correct_letter:
            self.feedback_label.config(text=f"✅ Correct! The answer is [{self.correct_answer}]", fg="green")
        else:
            self.feedback_label.config(text=f"❌ Wrong! Correct answer: [{self.correct_answer}]", fg="red")

        
        for btn in self.option_buttons:
            btn.config(state="disabled")

        
        self.root.after(2000, self.load_question)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
