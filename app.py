import streamlit as st
import random

# ==========================================
# MASTER QUESTION BANK
# ==========================================
MASTER_QUESTION_BANK = {
  
    "Operational Procedures": [
        # --- Multiple Choice Section ---
        {
            "question": "Who is responsible for reporting acts of unlawful interference?",
            "choices": ["The Commander or the Operator", "The ATCU for the airspace in which the event occurred", "Any member of the flight crew", "Any person on board the aeroplane"],
            "correct": "The Commander or the Operator"
        },
        {
            "question": "To act as co-pilot for take-off or landing, you must have:",
            "choices": ["Acted as PIC or co-pilot on type in the last 90 days", "Acted as PIC or co-pilot on type in the last 30 days", "Acted as PIC or co-pilot on type in the last 60 days", "Been at the controls for landing in the same type recently"],
            "correct": "Acted as PIC or co-pilot on type in the last 90 days"
        },
        {
            "question": "What is required for navigation in IMC?",
            "choices": ["Radio equipment and equipment for guidance until visual point", "Anti-icing equipment", "A serviceable weather radar", "One VHF box and one HF box"],
            "correct": "Radio equipment and equipment for guidance until visual point"
        },
        {
            "question": "What is the minimum visibility for a Cat A aircraft during a circling approach?",
            "choices": ["1500m", "1600m", "2400m", "3600m"],
            "correct": "1600m"
        },
        {
            "question": "When do you not need a destination alternate aerodrome?",
            "choices": ["If there is a reasonable certainty that at the ETA at the destination aerodrome and a reasonable time before and after you can expect VMC", "If the flight time is less than 6 hours", "If the flight time is less than 1 hour", "If your operator deems the weather to be suitable for a visual landing"],
            "correct": "If there is a reasonable certainty that at the ETA at the destination aerodrome and a reasonable time before and after you can expect VMC"
        },
        {
            "question": "When does a pilot apply the limitations of the MEL?",
            "choices": ["At parking before commencement of taxi", "Prior to take-off", "At any time in flight", "Any time up to coming to a complete stop and applying the parking brake"],
            "correct": "Any time up to coming to a complete stop and applying the parking brake"
        },
        {
            "question": "What is the minimum RVR for a CAT IIIC approach?",
            "choices": ["No minimum", "50m", "75m", "100m"],
            "correct": "No minimum"
        },
        {
            "question": "On an ILS approach, you are told that the weather has dropped below company minima. When must you abort the approach?",
            "choices": ["Start of the glide-slope descent", "FAF", "Inner marker", "Outer marker"],
            "correct": "Outer marker"
        },
        {
            "choices": ["Squawk 7700 if the situation requires and continue the flight as per the ATC clearance received if possible", "Squawk 7500 and broadcast a warning to ATC other traffic on 121.500MHz or the frequency in use whilst maintaining the flight as cleared", "Squawk 7500 (or 7700 if required) and broadcast a warning if the situation forces deviation from the cleared flight plan", "If forced to deviate from the flight plan, climb or descend to altitudes that differ from the normal cruising altitudes by 1000ft"],
            "question": "In the event of an act of unlawful interference, which of the following is the correct procedure to be taken by the pilot in command?",
            "correct": "Squawk 7500 (or 7700 if required) and broadcast a warning if the situation forces deviation from the cleared flight plan"
        },
        {
            "question": "A Flight Data Recorder is required in aeroplanes over:",
            "choices": ["20,000kg", "5,700kg", "10,000kg", "7,000kg"],
            "correct": "5,700kg"
        },
        {
            "question": "At the alternate aerodrome, the commander of a turbojet engine aeroplane should have a fuel quantity (final reserve) sufficient for flying during:",
            "choices": ["30 minutes at holding flight speed at 1,500 ft", "45 minutes at holding flight speed at 1,500 ft", "30 minutes at cruising speed", "45 minutes at cruising speed"],
            "correct": "30 minutes at holding flight speed at 1,500 ft"
        },
        {
            "question": "Aircrafts are categorized according to their threshold speeds, multiplied by a factor. What aircraft category corresponds to a range of speeds 141kts - 165kts?",
            "choices": ["Category B", "Category E", "Category D", "Category C"],
            "correct": "Category D"
        },
        {
            "question": "Where a light category aeroplane is landing behind a medium category aeroplane, minimum separation distance in NM is:",
            "choices": ["6 NM", "5 NM", "4 NM", "3 NM"],
            "correct": "5 NM"
        },
        {
            "question": "The method of alighting the aeroplane on water during a ditching is to:",
            "choices": ["Carry out a normal approach with flaps and gear selected as normal but to calculate all speeds plus 10kts", "Reduce the approach angle to 1.5deg (150ft/mile), add 15kts to all speeds, keep the aeroplane clean (no flaps or gear) and fly it into the surface", "Fly a normal approach but keep the gear up and land at lowest possible speed with the nose raised for the tail to strike first", "Fly a normal approach to stalling speed and then drop the aeroplane vertically onto the water"],
            "correct": "Fly a normal approach but keep the gear up and land at lowest possible speed with the nose raised for the tail to strike first"
        },
        {
            "question": "If the captain elects to ditch the aeroplane, it is recommended to:",
            "choices": ["Land along the swell", "Land into the swell but down wind", "Land into the swell but into wind", "Land into wind regardless of the swell direction if the wind speed is over 20kts"],
            "correct": "Land along the swell"
        },

        # --- Flashcard Section ---
        {
            "question": "What is the definition of the term 'viscous hydroplaning'?",
            "choices": [],
            "correct": "A film of moisture covers the painted or rubber-coated portion of the runway"
        },
        {
            "question": "Compared to dynamic hydroplaning, at what speed does viscous hydroplaning occur when landing on a smooth, wet runway?",
            "choices": [],
            "correct": "At a lower speed than dynamic hydroplaning"
        },
        {
            "question": "What is the best method of speed reduction if hydroplaning is experienced on landing?",
            "choices": [],
            "correct": "Apply aerodynamic braking to the fullest advantage"
        },
        {
            "question": "What effect, if any, will landing higher-than-recommended touchdown speed have on hydroplaning?",
            "choices": [],
            "correct": "Increases hydroplaning potential regardless of braking"
        },
        {
            "question": "Which is an effect of ice, snow, or frost formation on an airplane?",
            "choices": [],
            "correct": "Decreased angle of attack for stalls / Increased stall speed"
        },
        {
            "question": "Test data indicate that ice, snow or frost having a thickness and roughness similar to medium or coarse sandpaper on the leading edge and upper surface of the wing can reduce lift and increase drag by how much?",
            "choices": [],
            "correct": "Reduce lift by as much as 30% and increase drag by 40%"
        },
        {
            "question": "Freezing Point Depressant (FPD) fluids used for deicing are intended to provide protection during which phase?",
            "choices": [],
            "correct": "Are intended to provide ice protection on the ground only"
        },
        {
            "question": "What is the purpose of diluting ethylene glycol deicing fluid with water in non-precipitation conditions?",
            "choices": [],
            "correct": "Decrease the freeze point"
        },
        {
            "question": "What action should the pilot take when 'gate hold' procedures are in effect?",
            "choices": [],
            "correct": "Contact ground control prior to starting engine for sequencing"
        },
        {
            "question": "What is the pilot's responsibility for clearance or instruction readback?",
            "choices": [],
            "correct": "Except for SIDs, readback altitude assignments, altitude restrictions and vectors"
        },
        {
            "question": "What action should a pilot take if within 3 minutes of a clearance limit and further clearance has not been received?",
            "choices": [],
            "correct": "Start a speed reduction to holding speed in preparation for holding"
        },
        {
            "question": "Under what condition should a pilot on IFR advise ATC of minimum fuel status?",
            "choices": [],
            "correct": "If the remaining fuel precludes any undue delay"
        },
        {
            "question": "What is the international emergency transponder code for a hijack situation?",
            "choices": [],
            "correct": "7500"
        },
        {
            "question": "It is the responsibility of the pilot and crew to report a near mid-air collision as a result of proximity of at least what distance?",
            "choices": [],
            "correct": "500 feet or less to another aircraft"
        },
        {
            "question": "What operational data does TCAS II provide on the flight deck?",
            "choices": [],
            "correct": "Traffic and resolution advisories"
        },
        {
            "question": "Which reports are always required when on an IFR approach not in radar contact?",
            "choices": [],
            "correct": "Leaving FAF inbound or outer marker inbound and missed approach"
        },
        {
            "question": "If visual reference is lost while circling to land from an instrument approach, what actions should the pilot take?",
            "choices": [],
            "correct": "Make a climbing turn toward the landing runway until established on the missed approach course"
        },
        {
            "question": "What is the difference between a visual and a contact approach?",
            "choices": [],
            "correct": "A visual approach is initiated by ATC while a contact approach is initiated by the pilot"
        },
        {
            "question": "Which initial cockpit indication should a pilot be aware of when a constant tailwind shears to a calm wind?",
            "choices": [],
            "correct": "Altitude, pitch and indicated airspeed increase"
        },
        {
            "question": "How does the wake turbulence vortex circulate around each wingtip?",
            "choices": [],
            "correct": "Outward, upward and around the wingtip"
        },
        {
            "question": "What wind condition prolongs the hazard of wake turbulence on a landing runway for the longest period of time?",
            "choices": [],
            "correct": "Light quartering tailwind"
        }
    ],
    "Navigation": [
        # --- Multiple Choice Section ---
        {
            "question": "On receipt of a TCAS RA, your immediate action is to:",
            "choices": ["Initiate the required maneuver immediately", "Make a note of the details", "Request a flight clearance deviation from ATC", "Do nothing until a TA is received"],
            "correct": "Initiate the required maneuver immediately"
        },
        {
            "question": "Which of the following are all errors associated with ADF?",
            "choices": [
                "Selective availability, coastal refraction, night effect",
                "Night effect, quadrantal error, lane slip",
                "Mountain effect, station interference, static interference",
                "Selective availability, coastal refraction, quadrantal error"
            ],
            "correct": "Mountain effect, station interference, static interference"
        },
        {
            "question": "The sequence of marker colours when flying an ILS approach is:",
            "choices": ["White, blue, amber", "Blue, white, amber", "Blue, amber, white", "Amber, blue, white"],
            "correct": "Blue, amber, white"
        },
        {
            "question": "The FMC navigational database can be accessed by the pilots:",
            "choices": ["To update the database", "To read information only", "To change information between the 28 day updates", "To change the information to meet the sector requirements"],
            "correct": "To read information only"
        },
        {
            "question": "Which of the following is categorized as a primary radar system?",
            "choices": ["SSR", "DME", "GPS", "AWR"],
            "correct": "AWR"
        },
        {
            "question": "Which frequency band corresponds to a wavelength of 1200m?",
            "choices": ["UHF", "LF", "HF", "MF"],
            "correct": "LF"
        },
        {
            "question": "DME and VOR are 'frequency paired' because:",
            "choices": ["The same receiver can be used for both aids", "The VOR transmitter is easily converted to the required DME frequency", "Cockpit workload is reduced", "Both ground transmitter aerials can be placed on the same site if required"],
            "correct": "Cockpit workload is reduced"
        },
        {
            "question": "The frequency band of the ILS glidepath is:",
            "choices": ["UHF", "VHF", "SHF", "VLF"],
            "correct": "UHF"
        },
        {
            "question": "Which of the following scenarios would give the best indication of groundspeed?",
            "choices": ["A VOR on the flight plan route", "A VOR off the flight plan route", "A DME on the flight plan route", "A DME off the flight plan route"],
            "correct": "A DME on the flight plan route"
        },
        {
            "question": "At the magnetic equator:",
            "choices": ["Dip is zero", "Variation is zero", "Deviation is zero", "The isogonal is an agonic line"],
            "correct": "Dip is zero"
        },
        {
            "question": "An aircraft is tracking inbound to a VOR beacon on the 105 radial. The setting the pilot should put on the OBS and the resulting CDI indication are:",
            "choices": ["285, TO", "105, TO", "285, FROM", "105, FROM"],
            "correct": "285, TO"
        },
        {
            "question": "An aircraft heading 017° (T) has a small island showing on the AWR at 45nm range on the 60° left azimuth line. To obtain a fix from this information you should plot:",
            "choices": [
                "Range 45nm and QTE 060 from the center of the island",
                "Range 45nm and QTE 240 from the center of the island",
                "Range 45nm and QTE 317 from the center of the island",
                "Range 45nm and QTE 137 from the center of the island"
            ],
            "correct": "Range 45nm and QTE 137 from the center of the island"
        },
        {
            "question": "The DME counters are rotating continuously. This indicates that:",
            "choices": ["The DME is unserviceable", "The DME is trying to lock onto range", "The DME is trying to lock onto frequency", "The DME is receiving no response from the ground station"],
            "correct": "The DME is trying to lock onto range"
        },
        {
            "question": "With reference to Traffic Collision Avoidance Systems, the core difference between TCAS I and II is that:",
            "choices": [
                "TCAS II can provide Traffic Advisories and Resolution Advisories whilst TCAS I can only provide Traffic Advisories",
                "TCAS II can only be fitted to large aircrafts which carry more than 30 passengers",
                "TCAS I can be fitted to aircrafts with Mode A only while TCAS II requires Mode C or S",
                "TCAS II can only be fitted to aircraft which are equipped with EFIS"
            ],
            "correct": "TCAS II can provide Traffic Advisories and Resolution Advisories whilst TCAS I can only provide Traffic Advisories"
        },
        {
            "question": "At a range of 200nm from a VOR, if there is an error of 1°, how far off the centreline is the aircraft?",
            "choices": ["3.5nm", "1.75nm", "7nm", "1nm"],
            "correct": "3.5nm"
        },
        
        # --- Flashcard Section ---
        {
            "question": "What is the overall stated range accuracy limits associated with DME systems?",
            "choices": [],
            "correct": "±0.25nm ±1.25% of range"
        },
        {
            "question": "Where can the Inertial Reference System (IRS) position be updated?",
            "choices": [],
            "correct": "On the ground only (during the alignment procedure)"
        },
        {
            "question": "In a Doppler VOR (DVOR), what type of signal forms the reference signal and what forms the bearing signal?",
            "choices": [],
            "correct": "Reference signal is AM, bearing signal is FM (with anti-clockwise rotation)"
        },
        {
            "question": "An aircraft wishes to track a VOR along the 274 radial. If the local magnetic variation is 10° W, what value should be set on the OBS?",
            "choices": [],
            "correct": "094"
        },
        {
            "question": "An aircraft attempting to home to a VOR on the 064 radial sees a CDI showing 4 dots fly right with a TO indication at 45nm DME. Where is the aircraft relative to the track?",
            "choices": [],
            "correct": "3nm left of track"
        },
        {
            "question": "An aircraft is required to intercept and home to a VOR along the 064 radial. What should the OBS be set to for correct needle sense and a TO indication?",
            "choices": [],
            "correct": "244"
        },
        {
            "question": "The radar in an aircraft at FL370 detects a cloud at 60nm. The cloud disappears when the tilt is selected to 2° UP. If the beamwidth is 6°, at what altitude are the tops of the cloud?",
            "choices": [],
            "correct": "43,000ft"
        },
        {
            "question": "What is the correct format for the input of coordinates 50N 00527E into the CDU/FMC system?",
            "choices": [],
            "correct": "N5000.0E00527.0"
        },
        {
            "question": "An aircraft has to communicate with a VHF station at 300nm range. If the ground station is at 2,500ft AMSL, what is the lowest altitude contact can be expected?",
            "choices": [],
            "correct": "36,100ft"
        },
        {
            "question": "Which specific component associated with the ILS is identified by the first two letters of the localizer identification group?",
            "choices": [],
            "correct": "Outer compass locator"
        },
        {
            "question": "Which 'rule-of-thumb' may be used to approximate the rate of descent required for a standard 3° glidepath?",
            "choices": [],
            "correct": "5 times groundspeed in knots"
        },
        {
            "question": "What are the respective range limits for the front and back guidance coverage of a Microwave Landing System (MLS)?",
            "choices": [],
            "correct": "20NM front and 7NM back"
        },
        {
            "question": "At what point in flight phase transitions is the FMS/FMC position calculated to be at its least accurate?",
            "choices": [],
            "correct": "At Top of Descent (TOD)"
        },
        {
            "question": "What is the mandatory period of validity / update cycle for an FMS navigational database?",
            "choices": [],
            "correct": "28 days"
        },
        {
            "question": "As a convective storm cell intensifies, what color sequence shifts are displayed on a standard airborne AWR?",
            "choices": [],
            "correct": "Green, yellow, red"
        },
        {
            "question": "When an aircraft at FL360 is directly over a DME ground station situated at MSL, what range is displayed on the cockpit counter?",
            "choices": [],
            "correct": "6 nm (Slant Range)"
        },
        {
            "question": "What standard Morse code aural indication should be observed over the ILS outer marker position?",
            "choices": [],
            "correct": "Continuous dashes at the rate of two per second (with a blue light)"
        },
        {
            "question": "What are the lowest Category II (CAT II) minimums?",
            "choices": [],
            "correct": "DH 100 feet and RVR 1200 feet"
        },
        {
            "question": "What azimuth coverage can be expected from a standard Microwave Landing System (MLS)?",
            "choices": [],
            "correct": "Laterally 40° each side, vertically up to 15° or 20,000 feet, and a range of 20NM"
        }
    
    ],
   "Flight Performance & Planning": [
        # --- Multiple Choice Section ---
        {
            "question": "If a jet engine fails during take-off before V1:",
            "choices": [
                "The take-off can be continued or aborted",
                "The take-off should be aborted",
                "The take-off should be continued",
                "The take-off may be continued if the aircraft speed is above VMCG and lies between VGO and VSTOP"
            ],
            "correct": "The take-off should be aborted"
        },
        {
            "question": "When does THRUST = DRAG?",
            "choices": [
                "Climbing at a constant IAS",
                "Descending at a constant IAS",
                "Flying level at a constant IAS",
                "All of the above"
            ],
            "correct": "Flying level at a constant IAS"
        },
        {
            "question": "How many hours in advance of departure time should a flight plan be filed in the case of flights into areas subject to air traffic flow management (ATFM)?",
            "choices": ["3.00 hrs", "0.30 hrs", "1.00 hr", "0.10 hr"],
            "correct": "3.00 hrs"
        },
        {
            "question": "At a constant mass and altitude, a lower airspeed requires:",
            "choices": [
                "More thrust and a lower coefficient of lift",
                "Less thrust and a lower coefficient of lift",
                "More thrust and a lower coefficient of drag",
                "A higher coefficient of lift"
            ],
            "correct": "A higher coefficient of lift"
        },
        {
            "question": "When approaching a wet runway with the risk of hydroplaning, what technique should the pilot adopt?",
            "choices": [
                "Positive touchdown, full reverse and brakes as soon as possible",
                "Smoothest possible touchdown, full reverse and only brakes below VP",
                "Positive touchdown, full reverse and only brakes below VP",
                "Normal landing, full reverse brakes at VP"
            ],
            "correct": "Positive touchdown, full reverse and brakes as soon as possible"
        },
        {
            "question": "The best EAS/Drag ratio is approximately:",
            "choices": ["1.3 VMD", "1.32 VMD", "1.6 VMD", "1.8 VMD"],
            "correct": "1.32 VMD"
        },
        {
            "question": "What factors affect descent angle in a glide?",
            "choices": [
                "Configuration and altitude",
                "Configuration and angle of attack",
                "Mass and altitude",
                "Mass and configuration"
            ],
            "correct": "Configuration and angle of attack"
        },
        {
            "question": "At a fuel check you have 60 US gallons (USG) of usable fuel remaining. Alternative fuel required is 12USG. The flight time remaining is 1 hour 35 mins. What is the highest consumption rate acceptable?",
            "choices": ["33.0 USG/Hr", "37.9 USG/Hr", "30.3 USG/Hr", "21.3 USG/Hr"],
            "correct": "30.3 USG/Hr"
        },
        {
            "question": "Maximum endurance:",
            "choices": [
                "Can be achieved in level unaccelerated flight with minimum fuel consumption",
                "Can be achieved by flying at the best rate of climb speed in straight and level flight",
                "Can be achieved in a steady climb",
                "Can be achieved by flying at the absolute ceiling"
            ],
            "correct": "Can be achieved in level unaccelerated flight with minimum fuel consumption"
        },
        {
            "question": "By what percentage should V2 be greater than VMCA?",
            "choices": ["30%", "10%", "20%", "15%"],
            "correct": "10%"
        },
        {
            "question": "The maximum induced drag occurs at a speed of:",
            "choices": ["VMD", "VMP", "VSO", "VATO"],
            "correct": "VSO"
        },
        {
            "question": "Define the useful load:",
            "choices": [
                "traffic load plus dry operating mass",
                "traffic load plus usable fuel mass",
                "dry operating mass plus usable fuel load",
                "that part of the traffic load which generates revenue"
            ],
            "correct": "traffic load plus usable fuel mass"
        },
        {
            "question": "How is fuel consumption affected by the C of G position, in terms of ANM/kg?",
            "choices": [
                "Increases with a forward C of G",
                "Decreases with an aft C of G",
                "Decreases with a forward C of G",
                "Fuel consumption is not affected by the C of G position"
            ],
            "correct": "decreases with a forward C of G"
        },
        {
            "question": "For take-off performance calculations, what is taken into account?",
            "choices": [
                "OAT, pressure altitude, wind, weight",
                "Standard temperature, altitude, wind, weight",
                "Standard altitude, standard temperature, wind, weight",
                "Standard temperature, pressure altitude, wind, weight"
            ],
            "correct": "OAT, pressure altitude, wind, weight"
        },
        {
            "question": "Refer to weather information for Birmingham: SA0850 280850 18014kt 9999 SCT024 BKN030 BKN045... FC0600 280600Z 280816... TEMPO 0812... BECMG 1214... FT0400 280434Z 281212 19022G37 9999 BKN025 TEMPO 1902 5000 RA BKN010 BECMG 2201 25007KT. What is the total time for which the weather is forecast?",
            "choices": ["9 hours", "18 hours", "24 hours", "28 hours"],
            "correct": "28 hours"
        },
        {
            "question": "When does the first segment of the take-off climb begin?",
            "choices": ["When V2 is reached", "When 35 feet is reached", "When flaps are up", "When gear and flaps are up"],
            "correct": "When 35 feet is reached"
        },
        {
            "question": "For a flight plan filed before flight, the indicated time of departure is:",
            "choices": [
                "The time overhead the first reporting point after take-off",
                "The time at which the flight plan is filed",
                "The estimated off-block time",
                "The time of take-off"
            ],
            "correct": "the estimated off-block time"
        },
        {
            "question": "Given: True track 215; mountain elevation 11,600ft; local airfield gives QNH as 1035mb; required terrain clearance 1500ft; temperature ISA -15C. Which of the following is the minimum flight level considering the temperature?",
            "choices": ["FL150", "FL140", "FL120", "FL110"],
            "correct": "FL140"
        },
        {
            "question": "After flying for 16 minutes at 100kt TAS with a 20kt tail wind, you have to return to the airfield of departure. You will arrive after:",
            "choices": ["10 min 40 sec", "20 min", "24 min", "16 min"],
            "correct": "24 mins"
        },

        # --- Flashcard Section ---
        {
            "question": "When submitting an operational flight plan before a flight, how is the departure time defined?",
            "choices": [],
            "correct": "at which the aircraft leaves the parking area"
        },
        {
            "question": "What is the Total Elapsed Time definition on a VFR flight plan?",
            "choices": [],
            "correct": "From take-off to overhead destination"
        },
        {
            "question": "In flight, what four operations are officially possible regarding a flight plan according to Rules of the Air?",
            "choices": [],
            "correct": "file an IFR flight plan, modify an active flight plan, cancel a VFR flight plan, and close a VFR flight plan"
        },
        {
            "question": "If a pilot lands at an alternate aerodrome other than the destination specified in the ICAO flight plan, within what time must the destination ATS unit be informed?",
            "choices": [],
            "correct": "30 mins"
        },
        {
            "question": "Define useful load using operational weights.",
            "choices": [],
            "correct": "TOM minus the DOM"
        },
        {
            "question": "At what operational milestone does the first segment of the take-off flight path end?",
            "choices": [],
            "correct": "at completion of gear retraction"
        },
        {
            "question": "For a turbojet aeroplane, when does the second segment of the climb begin?",
            "choices": [],
            "correct": "Landing gear is fully retracted"
        },
        {
            "question": "For a turbojet aeroplane, when does the third segment of the climb begin?",
            "choices": [],
            "correct": "Acceleration to a flap retraction speed begins (min 400ft)"
        },
        {
            "question": "Which specific airspeed or coefficient gives an aircraft its greatest gliding endurance?",
            "choices": [],
            "correct": "Flight close to CL MAX"
        },
        {
            "question": "What is characteristic of longitudinal instability during flight?",
            "choices": [],
            "correct": "pitch oscillations becoming progressively greater"
        },
        {
            "question": "What specific operational factors affect an aircraft's indicated stall speed?",
            "choices": [],
            "correct": "weight load factor and power"
        },
        {
            "question": "What performance and stability characteristics are associated with an aircraft loaded to its absolute aft CG limit?",
            "choices": [],
            "correct": "lowest stall speed, highest cruise speed and least stability"
        },
        {
            "question": "What effect does an upward runway slope have on take-off performance metrics?",
            "choices": [],
            "correct": "increases takeoff distance required"
        },
        {
            "question": "At what speed relative to L/D max does the maximum rate of climb for a jet airplane occur?",
            "choices": [],
            "correct": "a speed greater than that for L/D max"
        },
        {
            "question": "How do the rate of turn and radius of turn change if bank angle is held constant while airspeed is increased?",
            "choices": [],
            "correct": "rate will decrease but radius will increase"
        },
        {
            "question": "If an aircraft with a gross weight of 2,000 pounds is subjected to a total load of 6,000 pounds in flight, what is the resulting load factor?",
            "choices": [],
            "correct": "3G'S"
        },
        {
            "question": "What is the 'Total Elapsed Time' for an IFR flight when filling in box 16 of the ICAO flight plan?",
            "choices": [],
            "correct": "take-off until reaching the IAF (Initial Approach Fix) of the destination aerodrome"
        }
    ],
    "Aircraft General Knowledge": [],
    "Aircraft General Knowledge": [
        # --- Multiple Choice Section ---
        {
            "question": "CAS is IAS corrected for:",
            "choices": [
                "Position and instrument error",
                "Instrument, pressure, and density error",
                "Relative density only",
                "Compressibility"
            ],
            "correct": "Position and instrument error"
        },
        {
            "question": "With an almost discharged battery there will be:",
            "choices": [
                "A decrease of voltage with increasing load",
                "Increase of current with decrease of voltage",
                "Decrease of current with increasing load",
                "Increase of voltage with increasing load"
            ],
            "correct": "A decrease of voltage with increasing load"
        },
        {
            "question": "At what height is it mandatory for one flight crew member on the flight deck to wear an oxygen mask?",
            "choices": ["25,000ft", "32,000ft", "37,000ft", "41,000ft"],
            "correct": "41,000ft"
        },
        {
            "question": "When would the negative differential pressure limits be reached/exceeded?",
            "choices": [
                "Rapid descent when AC descends below cabin altitude",
                "During ground pressure testing",
                "Rapid ascent when aircraft climbs",
                "When changing to manual operation"
            ],
            "correct": "Rapid descent when AC descends below cabin altitude"
        },
        {
            "question": "Maximum Differential pressure:",
            "choices": [
                "Is the maximum authorized pressure difference between the inside of the fuselage and the atmospheric ambient pressure",
                "Is the absolute pressure provided by the vacuum pump",
                "Is the pressure loss over a given time limit",
                "Is the absolute pressure the cabin pressure ducting is designed to carry"
            ],
            "correct": "Is the maximum authorized pressure difference between the inside of the fuselage and the atmospheric ambient pressure"
        },
        {
            "question": "Cabin altitude in pressurized flight is:",
            "choices": [
                "The altitude corresponding to cabin pressure regardless of aircraft height",
                "Is presented on a second needle on the aircraft altimeter",
                "Altitude at which cabin pressure equals ambient pressure",
                "Altitude corresponding to cabin pressure in relation to MSL ISA conditions"
            ],
            "correct": "The altitude corresponding to cabin pressure regardless of aircraft height"
        },
        {
            "question": "With a gas turbine engine, engine anti-icing should be selected 'ON':",
            "choices": [
                "Whenever the igniters are on",
                "Whenever the IOAT is +10°C or below and the air contains visible moisture",
                "Whenever the TOAT is +10°C or below and it is raining",
                "Whenever the ice detector system warning light comes on"
            ],
            "correct": "Whenever the IOAT is +10°C or below and the air contains visible moisture"
        },
        {
            "question": "Which of the following instruments require inputs of both pitot and static pressure?",
            "choices": [
                "Airspeed indicator, machmeter and vertical speed indicator",
                "Airspeed indicator, vertical speed indicator, altimeter",
                "Airspeed indicator only",
                "Airspeed indicator and machmeter"
            ],
            "correct": "Airspeed indicator and machmeter"
        },
        {
            "question": "When smoke appears in the cockpit, after donning the oxygen mask the pilot should select:",
            "choices": ["Normal", "100%", "Diluter", "Emergency"],
            "correct": "100%"
        },
        {
            "question": "When is spark plug fouling most likely to occur?",
            "choices": [
                "In the climb if you have not adjusted the mixture",
                "Cruise power",
                "In the descent if you have not adjusted the mixture",
                "Max take-off power"
            ],
            "correct": "In the descent if you have not adjusted the mixture"
        },
        {
            "question": "If a CSD overheat warning is shown:",
            "choices": [
                "The CSD can be disconnected and the pilot must control the alternator himself",
                "The pilot must throttle back to reduce the load on the alternator",
                "The CSD can be disconnected then reconnected later when the temperature has reduced",
                "The CSD can be disconnected but not used for the rest of the flight"
            ],
            "correct": "The CSD can be disconnected but not used for the rest of the flight"
        },
        {
            "question": "When does the engine High Pressure fuel shut off valve close?",
            "choices": [
                "After a booster pump failure",
                "When the engine fuel switch is selected 'ON' during engine start",
                "When flight idle is selected",
                "When the engine fuel switch is selected 'OFF' during engine down"
            ],
            "correct": "When the engine fuel switch is selected 'OFF' during engine down"
        },
        {
            "question": "The LED indicator on the emergency torch is flashing at 4 seconds intervals. This indicates:",
            "choices": [
                "The battery is charging",
                "The torch is serviceable",
                "The battery needs replacing",
                "The filament is broken"
            ],
            "correct": "The torch is serviceable"
        },
        {
            "question": "A shuttle valve will:",
            "choices": [
                "Allow the accumulator to be emptied after engine shut down",
                "Reduce pump loading when normal system pressure is reached",
                "Automatically switch to a more appropriate source of hydraulic supply",
                "Operate on a rising pressure, higher than the Full Flow relief valve"
            ],
            "correct": "Automatically switch to a more appropriate source of hydraulic supply"
        },
        {
            "question": "What is the purpose of inboard ailerons?",
            "choices": [
                "To reduce wing bending at high speed",
                "To reduce wing twisting at low speed",
                "To reduce wing bending at low speed",
                "To reduce wing twist at high speed"
            ],
            "correct": "To reduce wing twist at high speed"
        },
        {
            "question": "In what range is GPWS operative?",
            "choices": ["24500 ft", "3000-50 ft", "2450-50 ft", "30000 ft"],
            "correct": "2450-50 ft"
        },
        {
            "question": "A nose wheel control system:",
            "choices": [
                "Prevents the nosewheel from castering at all times",
                "Allows the nosewheel to caster within preset limits about the neutral position",
                "Allows the nosewheel to caster freely at all times",
                "Prevents the nose gear from lowering if the nosewheels are not centralized"
            ],
            "correct": "Allows the nosewheel to caster within preset limits about the neutral position"
        },
        {
            "question": "At an aircraft taxiing speed of 10mph, the anti-skid braking system is:",
            "choices": [
                "Inoperative",
                "Operative",
                "Operative only on the nosewheel brakes",
                "Operative only on the main wheel brakes"
            ],
            "correct": "Inoperative"
        },
        {
            "question": "A pressure head is subject to the following errors:",
            "choices": [
                "Position, manoeuvre induced, temperature",
                "Position, manoeuvre induced",
                "Position, manoeuvre induced, density",
                "Position, manoeuvre induced, instrument"
            ],
            "correct": "Position, manoeuvre induced"
        },
        {
            "question": "Total Air Temperature is:",
            "choices": [
                "The maximum temperature attainable by the air when brought to rest, adiabatically",
                "The temperature indicated on the air temperature thermometer plus the ram rise",
                "The static air temperature minus the recovery factor",
                "The recovery factor plus the ram rise"
            ],
            "correct": "The maximum temperature attainable by the air when brought to rest, adiabatically"
        },
        {
            "question": "When entering a steep turn, an IVSI is likely to show:",
            "choices": [
                "No change in altitude",
                "A slight climb",
                "A slight descent",
                "A slight descent at high airspeed only"
            ],
            "correct": "A slight climb"
        },
        {
            "question": "An aircraft is flying at constant indicated altitude over a warm airmass. The altimeter reading will be:",
            "choices": [
                "Correct",
                "Greater than the real altitude",
                "Less than the real altitude",
                "Oscillating around the correct altitude"
            ],
            "correct": "Less than the real altitude"
        },
        {
            "question": "An aircraft is travelling at 120 kts, what angle of bank would be required for a rate 1 (one) turn?",
            "choices": ["30°", "12°", "18°", "35°"],
            "correct": "18°"
        },
        {
            "question": "An aircraft is travelling at 100kts forward speed on a 3° glideslope. What is its rate of descent?",
            "choices": ["500 ft/min", "300 ft/min", "250 ft/min", "600 ft/min"],
            "correct": "500 ft/min"
        },
        {
            "question": "You are flying at a constant FL 290 and a constant mach number. The total temperature increases by 5°. The CAS will:",
            "choices": [
                "Remain approximately constant",
                "Increase by 10 kts",
                "Decrease by 10 kts",
                "Will increase or decrease depending on whether you are above or below ISA"
            ],
            "correct": "Remain approximately constant"
        },
        {
            "question": "With air in the hydraulic system, you would expect it to:",
            "choices": [
                "Operate normally because operation would remove it",
                "Have spongy operation and slower cycle runs",
                "Automatically purge via the accumulator line",
                "Operate significantly faster due to reduced density"
            ],
            "correct": "Have spongy operation and slower cycle runs"
        },
        {
            "question": "A hand pump is usually fitted to a hydraulic system:",
            "choices": [
                "For ground servicing purposes",
                "Lowering the landing gear in an emergency",
                "Pressurising the oleo struts in the air",
                "Retracting the gear after take-off"
            ],
            "correct": "For ground servicing purposes"
        },
        {
            "question": "What controls cabin pressurisation?",
            "choices": [
                "ECS pack mass flow controller",
                "Outflow valve",
                "Engine bleed valve",
                "Inflow valve"
            ],
            "correct": "Outflow valve"
        },
        {
            "question": "The EGT indication on a piston engine is used:",
            "choices": [
                "To control the cooling air shutters",
                "To monitor the oil temperature",
                "To assist the pilot to adjust the fuel mixture",
                "To indicate cylinder head temperature"
            ],
            "correct": "To assist the pilot to adjust the fuel mixture"
        },
        {
            "question": "The magnetic heading reference unit has a precision rate of:",
            "choices": ["1°/min", "2°/min", "5°/min", "3°/min"],
            "correct": "2°/min"
        },
        {
            "question": "How do you control power in a jet engine?",
            "choices": [
                "By controlling the mixture ratio",
                "By controlling the fuel flow",
                "By controlling the airflow",
                "By controlling the bleed valves"
            ],
            "correct": "By controlling the fuel flow"
        },
        {
            "question": "What type of autoland system would be required for the landing to continue following a single failure below alert height?",
            "choices": [
                "Fail soft",
                "Fail passive",
                "Fail operational or fail active",
                "Land 2 system"
            ],
            "correct": "Fail operational or fail active"
        },
        {
            "question": "If cabin pressure is decreasing, the cabin VSI will indicate:",
            "choices": ["Zero", "Climb", "Descent", "Reducing pressure"],
            "correct": "Climb"
        },
        {
            "question": "The purpose of a hydraulic accumulator is to:",
            "choices": [
                "Relieve excess pressure",
                "Store fluid under pressure",
                "Store compressed gas for tyre inflation",
                "Remove air from the system"
            ],
            "correct": "Store fluid under pressure"
        },
        {
            "question": "How much fuel can be jettisoned via a standard jettison configuration system?",
            "choices": [
                "A specific amount chosen manually on a slider scale",
                "The captain can drain all contents down to absolute empty tanks",
                "All contents except a specified amount that must remain inside the tanks",
                "Only fuel contained within the center wing tanks"
            ],
            "correct": "A specified amount must remain"
        },
        {
            "question": "What do three green lights represent when the landing gear is selected down?",
            "choices": [
                "The gear is down",
                "The gear is down and locked",
                "The gear and doors are down and locked",
                "The gear is travelling between up and down"
            ],
            "correct": "The gear is down and locked"
        },
        {
            "question": "The most likely cause of brake fade is:",
            "choices": [
                "Oil or grease on the brake drums",
                "Worn stators",
                "The pilot reducing the brake pressure",
                "The brake pads overheating"
            ],
            "correct": "The brake pads overheating"
        },
        {
            "question": "A cylinder head temperature gauge measures:",
            "choices": [
                "The temperature of the hottest cylinder",
                "The temperature of all the cylinders and gives an average reading",
                "The temperature of the coolest cylinder",
                "The temperature of the two cylinders furthest away from each other divided by two"
            ],
            "correct": "The temperature of the hottest cylinder"
        },
        {
            "question": "The excess cabin altitude alerting system must operate to warn the crew at:",
            "choices": ["8,000ft", "10,000ft", "13,000ft", "14,000ft"],
            "correct": "10,000ft"
        },
        {
            "question": "Under normal operating conditions, which combination of MAP and RPM produces the most severe wear, fatigue, and damage to high-performance reciprocating engines?",
            "choices": [
                "High RPM and low MAP",
                "Low RPM and high MAP",
                "High RPM and high MAP"
            ],
            "correct": "High RPM and high MAP"
        },
        {
            "question": "What effect does high relative humidity have upon the maximum power output of modern aircraft engines?",
            "choices": [
                "Reciprocating engines will experience a significant loss of BHP",
                "Turbine engines will trigger automatic bleed limiters",
                "No physical effect can be traced to humidity factors"
            ],
            "correct": "Reciprocating engines will experience a significant loss of BHP"
        },
        {
            "question": "What is controlled by the waste gate of a turbocharged-reciprocating engine?",
            "choices": [
                "Exhaust gas discharge",
                "Compressor bleed trim cycles",
                "Fuel-to-air induction matching profiles"
            ],
            "correct": "Exhaust gas discharge"
        },
        {
            "question": "What does a blue radial line on the airspeed indicator of a light, twin-engine airplane represent?",
            "choices": [
                "Never-exceed velocity limit under multi-engine runs",
                "Maximum single-engine rate of climb speed (VYSE)",
                "Minimum control speed with critical engine unserviceable"
            ],
            "correct": "Maximum single-engine rate of climb speed (VYSE)"
        },
        {
            "question": "What minimum flight performance should a pilot of a light, twin-engine airplane be able to maintain at Vmc?",
            "choices": ["Altitude", "Heading", "Positive climb profile"],
            "correct": "Heading"
        },
        {
            "question": "What effect, if any, does altitude have on Vmc for an airplane with unsupercharged engines?",
            "choices": [
                "Increases with altitude",
                "Decreases with altitude",
                "Remains constant across all heights"
            ],
            "correct": "Decreases with altitude"
        },
        {
            "question": "What criteria determines which engine is the 'critical' engine of a twin-engine airplane?",
            "choices": [
                "The engine turning opposite to the propeller rotation torque axis",
                "The one with the center of thrust closest to the centreline of the fuselage",
                "The engine whose breakdown creates the most immediate electrical load loss"
            ],
            "correct": "The one with the center of thrust closest to the centreline of the fuselage"
        },
        {
            "question": "Which condition has the effect of reducing critical engine failure speed during take-off runs?",
            "choices": [
                "High tire pressure limits",
                "Slush on the runway or inoperative antiskid",
                "Operating with a strict forward center of gravity location"
            ],
            "correct": "Slush on the runway or inoperative antiskid"
        },
        {
            "question": "Equivalent shaft horsepower (ESHP) of a turboprop engine is a measure of:",
            "choices": [
                "Shaft horsepower and jet thrust",
                "Propeller blade pitch resistance parameters",
                "Total internal core pressure altitude equivalents"
            ],
            "correct": "Shaft horsepower and jet thrust"
        },
        {
            "question": "Minimum specific fuel consumption of a turboprop engine is normally available in which altitude range?",
            "choices": [
                "Sea level up to 10,000 feet",
                "15,000 feet to 22,000 feet",
                "25,000 ft to the tropopause"
            ],
            "correct": "25,000 ft to the tropopause"
        },
        {
            "question": "What recovery procedure would be appropriate in the event of an active compressor stall?",
            "choices": [
                "Increase fuel flow rapidly and pitch up to load the wings",
                "Reduce fuel flow, reduce angle of attack, and increase airspeed",
                "Disengage bleed valves and select maximum continuous thrust power"
            ],
            "correct": "Reduce fuel flow, reduce angle of attack, and increase airspeed"
        },
        {
            "question": "Within what mach range does the transonic flight regime usually occur?",
            "choices": [
                "Below .75 Mach",
                ".75 to 1.20 Mach",
                "1.20 to 2.50 Mach"
            ],
            "correct": ".75 to 1.20 Mach"
        },
        {
            "question": "What is the free stream Mach number which produces the first evidence of local sonic flow over an airfoil surface?",
            "choices": [
                "Critical Mach number",
                "Transonic boundary speed",
                "Mach Buffet threshold"
            ],
            "correct": "Critical Mach number"
        },

        # --- Flashcard Section ---
        {
            "question": "How is boundary layer control accomplished using air injection streams?",
            "choices": [],
            "correct": "injecting a high speed jet of air into the boundary layer"
        },
        {
            "question": "On most airplanes, how does the first 50% of flap deflection affect lift parameters?",
            "choices": [],
            "correct": "causes more than 50% total change in lift"
        },
        {
            "question": "What performance cost do swept wing configurations impose on high-lift trailing edge flaps?",
            "choices": [],
            "correct": "a significant reduction in effectiveness of flaps"
        },
        {
            "question": "At what milestone point must the wing lift coefficient be at its absolute maximum value?",
            "choices": [],
            "correct": "airplane stall speed"
        },
        {
            "question": "How does weight alter the gliding performance profile of an airplane operating at L/D max?",
            "choices": [],
            "correct": "the airplane will have the same gliding performance at all weights"
        },
        {
            "question": "What primary sensory data must an airframe stall warning system monitor?",
            "choices": [],
            "correct": "pressure distribution"
        },
        {
            "question": "What fundamental pilot control input is required to successfully recover from an aerodynamic stall?",
            "choices": [],
            "correct": "decreasing the angle of attack"
        },
        {
            "question": "How does indicated stall speed (Vs) vary across changing pressure altitudes?",
            "choices": [],
            "correct": "varies directly with altitude"
        },
        {
            "question": "How does the never-exceed speed limit (VNE) change as flight altitude increases?",
            "choices": [],
            "correct": "VNE decreases with increasing altitude"
        },
        {
            "question": "What mechanical design subsystem prevents turbine engines from developing localized compressor stalls?",
            "choices": [],
            "correct": "compressor bleed valves"
        },
        {
            "question": "Compare split flaps to standard plain flaps regarding aerodynamic output variations.",
            "choices": [],
            "correct": "produce only slightly more lift, but much more drag"
        },
        {
            "question": "Compare the pitching moments produced by Fowler flaps against standard split flaps.",
            "choices": [],
            "correct": "generate more nose down pitching moment"
        },
        {
            "question": "When are outboard ailerons active on aircraft equipped with split inboard/outboard systems?",
            "choices": [],
            "correct": "low-speed flight only"
        },
        {
            "question": "Why are outboard ailerons typically locked out or deactivated during high-speed cruise phases?",
            "choices": [],
            "correct": "aerodynamic loads on the outboard ailerons tend to twist the wingtips at high speeds"
        },
        {
            "question": "What is the structural purpose of a auxiliary control tab?",
            "choices": [],
            "correct": "move the flight controls in an event of manual reversion"
        },
        {
            "question": "In which direction relative to the primary flight control surface does a servo tab deflect?",
            "choices": [],
            "correct": "opposite direction"
        },
        {
            "question": "In which direction relative to the primary flight control surface does an anti-servo tab deflect?",
            "choices": [],
            "correct": "same direction"
        },
        {
            "question": "What is the functional purpose of high-lift devices on clean wing structures?",
            "choices": [],
            "correct": "increase the lift at low speeds"
        },
        {
            "question": "What aerodynamic purpose do leading-edge wing slots serve?",
            "choices": [],
            "correct": "change the stalling angle of attack to a higher angle"
        },
        {
            "question": "What aerodynamic purpose do flight spoilers serve during descent profiles?",
            "choices": [],
            "correct": "reduce lift without increasing airspeed"
        },
        {
            "question": "What function do wing-mounted vortex generators perform regarding high-speed boundary flows?",
            "choices": [],
            "correct": "reduce drag caused by supersonic flow over portions of the wing"
        },
        {
            "question": "Where is the critical altitude line located for supercharged reciprocating aviation engines?",
            "choices": [],
            "correct": "the highest altitude at which the desired manifold pressure can be obtained"
        },
        {
            "question": "What total engine-out climb performance percentage loss can be expected if one engine fails on a light twin aircraft?",
            "choices": [],
            "correct": "reduction of climb by 50% or more"
        },
        {
            "question": "Which specific zone inside a gas turbine engine core is subjected to the absolute highest thermal temperatures?",
            "choices": [],
            "correct": "turbine inlet"
        },
        {
            "question": "What is the single most critical limit restriction to the safe operational running of turbojet engines?",
            "choices": [],
            "correct": "limiting exhaust gas temperature"
        },
        {
            "question": "What auditory and tactile symptoms characterize a transient engine compressor stall?",
            "choices": [],
            "correct": "imminent 'bang' as backfires and flow reversals take place"
        },
        {
            "question": "What symptoms identify a compressor stall that has developed and become fully steady?",
            "choices": [],
            "correct": "strong vibrations and loud roar"
        },
        {
            "question": "What operational movement does the center of pressure undergo if the wingtips of a swept wing shock-stall before the root?",
            "choices": [],
            "correct": "inward and forward"
        },
        {
            "question": "What is the main aerodynamic advantage of a sweptback wing structure over a straight wing design?",
            "choices": [],
            "correct": "the critical Mach number will increase significantly"
        },
        {
            "question": "What specific stall vulnerability is considered a major disadvantage of sweptwing structures?",
            "choices": [],
            "correct": "the wingtip section stalls prior to the wing root"
        },
        {
            "question": "What combined directional rolling and yawing instability is caused by sudden atmospheric gusts hitting sweptwing aircraft?",
            "choices": [],
            "correct": "Dutch roll"
        },
        {
            "question": "How should thrust reversers be operated immediately upon landing to maximize deceleration efficiency?",
            "choices": [],
            "correct": "immediately after ground contact"
        },
        {
            "question": "If both the ram air input hole and the drain hole of a pitot tube are fully blocked by ice during an enroute descent, what will the airspeed indicator do?",
            "choices": [],
            "correct": "the airspeed indicator may act as an altimeter"
        },
        {
            "question": "If the ram air input hole to a pitot head is blocked by ice while its drain hole and the static port remain clear, what indication will be displayed?",
            "choices": [],
            "correct": "indication will drop to zero"
        }
    ],
      "Wagyu?": [
        {
            "question": "Does David love Stephanie?",
            "choices": ["A little bit...", "ABSOLUTELY YES!", "Not so much...", "So-so..."],
            "correct": "ABSOLUTELY YES!"
        },

        {
            "question": "Where are David and Stephanie going to in February?",
            "choices": [],
            "correct": "Thailand!"
        },
        
    ],
    "Air Law": [
        # --- Multiple Choice Section ---
        {
            "question": "Except when cleared by an ATC unit, a VFR flight cannot enter or leave a Control Zone when the cloud base is lower than:",
            "choices": [
                "1000 feet and less than 8km visibility",
                "2000 feet and less than 5km visibility",
                "1500 feet or less than 5km visibility",
                "1000 feet and less than 5km visibility"
            ],
            "correct": "1500 feet or less than 5km visibility"
        },
        {
            "question": "What action should be taken when, during an IFR flight in VMC, you suffer a radio failure?",
            "choices": [
                "Return to the aerodrome from which you departed",
                "Continue flying in VMC and land as soon as possible",
                "Maintain your assigned altitude and land at the nearest aerodrome at which there are VMC conditions",
                "Continue flying at your assigned altitude and start your approach at your ETA"
            ],
            "correct": "Continue flying in VMC and land as soon as possible"
        },
        {
            "question": "For a controlled flight before departure, a flight plan must be filed at least:",
            "choices": [
                "50 minutes before off-block time",
                "60 minutes before departure",
                "10 minutes before departure",
                "30 minutes before off-block time"
            ],
            "correct": "30 minutes before off-block time"
        },
        {
            "question": "A controlled flight is required to inform the concerned ATC unit when the average TAS at cruising level deviates or is expected to deviate compared to that given TAS in the Flight Plan by at least plus or minus:",
            "choices": ["10%", "3%", "5%", "2%"],
            "correct": "5%"
        },
        {
            "question": "What is the rule concerning level or height the aircraft should maintain when flying IFR outside controlled airspace unless otherwise directed?",
            "choices": [
                "2,000 feet above the highest obstacle within 8kms of the heading",
                "1,500 feet above the highest obstacle within 5kms of the estimated position",
                "1,000 feet above the highest obstacle within 8kms of the estimated position of the aircraft",
                "1,000 feet above the highest obstacle within 5kms of the planned track"
            ],
            "correct": "1,000 feet above the highest obstacle within 8kms of the estimated position of the aircraft"
        },
        {
            "question": "If the track on an instrument departure is published, the pilot is expected to:",
            "choices": [
                "Correct for the correct wind so as to stay within controlled airspace",
                "Ask ATC for another heading to steer correcting for wind",
                "Ignore the wind and proceed with a heading equal to the track",
                "Ask ATC for permission to correct heading for wind"
            ],
            "correct": "Correct for the correct wind so as to stay within controlled airspace"
        },
        {
            "question": "When the Captain cannot comply with an ATC clearance:",
            "choices": [
                "The Captain must accept the ATC clearance, because it is based on a filed flight plan",
                "He/she may request an amended clearance and, if executable, he/she will accept that clearance",
                "He/she may ask a new clearance and the appropriate ATC must grant him/her that clearance",
                "He/she may suggest a new clearance to ATC"
            ],
            "correct": "He/she may request an amended clearance and, if executable, he/she will accept that clearance"
        },
        {
            "question": "An aircraft is allowed to descend below the MSA if:",
            "choices": [
                "The pilot follows the published approach procedures",
                "The aircraft receives radar vectors",
                "The pilot has visual contact with the runway and surrounding terrain and is able to maintain visual contact",
                "All of the above"
            ],
            "correct": "All of the above"
        },
        {
            "question": "What is required for an IFR flight in advisory airspace?",
            "choices": [
                "No flight plan required",
                "Flight plan required and PIC must notify of any changes regardless if wanting advisory service or not",
                "Flight plan required but PIC need not notify of any changes",
                "A flight plan is only required if advisory service is required"
            ],
            "correct": "Flight plan required and PIC must notify of any changes regardless if wanting advisory service or not"
        },
        {
            "question": "What are the VMC limits for Class B airspace?",
            "choices": [
                "8km flight visibility, clear of cloud and in sight of the surface",
                "8km flight visibility, 1000ft vertically and 1500m horizontally from cloud",
                "5km flight visibility, 1000ft vertically and 1500m horizontally from cloud",
                "The same as Class D"
            ],
            "correct": "8km flight visibility, 1000ft vertically and 1500m horizontally from cloud"
        },
        {
            "question": "A Precision Approach Procedure is defined as:",
            "choices": [
                "An approach using bearing, elevation and distance information",
                "An approach with a crew of at least 2 pilots trained for such operations",
                "An instrument approach procedure utilizing azimuth and glide path information provided by an ILS or a PAR",
                "An approach using bearing, elevation, and, optionally, distance information"
            ],
            "correct": "An instrument approach procedure utilizing azimuth and glide path information provided by an ILS or a PAR"
        },
        {
            "question": "An instrument approach is made up of a number of segments. How many of them are there?",
            "choices": ["4", "5", "3", "6"],
            "correct": "5"
        },
        {
            "question": "An aircraft flying over the sea between 4500ft and 9000ft AMSL and outside CAS. To continue under VFR the meteorological conditions must remain:",
            "choices": [
                "2000ft horizontally and 1000ft vertically from cloud with visibility of 8km",
                "1500m horizontally and 1000ft vertically from cloud with visibility of 5km",
                "1500m horizontally and 1000m vertically from cloud with visibility of 5km",
                "Clear of cloud and in sight of the surface with visibility of 5km"
            ],
            "correct": "1500m horizontally and 1000ft vertically from cloud with visibility of 5km"
        },
        {
            "question": "Which Mode A code must be used to make sure that your aircraft is recognized as an aircraft in distress?",
            "choices": ["Code 7500", "Code 7700", "Code 7000", "Code 7600"],
            "correct": "Code 7700"
        },
        {
            "question": "What action should be taken if contact is lost with the runway during a circling approach?",
            "choices": [
                "Descend to Decision Height and if still no contact with the runway, initiate a missed approach",
                "Land on the instrument runway",
                "Initiate a missed approach",
                "Return to the FAF"
            ],
            "correct": "Initiate a missed approach"
        },
        {
            "question": "The longitudinal separation minimum based on time between aircrafts at the same FL, where there is enough coverage for navigation aids and the preceding aircraft has a higher true airspeed of 20kts minimum is:",
            "choices": ["3 minutes", "15 minutes", "5 minutes", "10 minutes"],
            "correct": "5 minutes"
        },
        {
            "question": "Repetitive flight plans (RPL's) cannot be used for flights other than those executed frequently on the same days of the following weeks and:",
            "choices": [
                "For at least 20 occasions or every day over a period of at least 20 consecutive days",
                "For at least 20 consecutive days",
                "For at least 10 occasions or every day over a period of at least 10 consecutive days",
                "For at least 20 occasions"
            ],
            "correct": "For at least 10 occasions or every day over a period of at least 10 consecutive days"
        },
        {
            "question": "Operationally significant changes to AIP shall be published in accordance with:",
            "choices": ["AIC's", "AIP Supplements", "AIRAC procedures", "Trigger NOTAMS"],
            "correct": "AIRAC procedures"
        },
        {
            "question": "When the aircraft carries a serviceable Mode C transponder, the pilot shall continuously operate this mode:",
            "choices": [
                "Only when directed by ATC",
                "Unless otherwise directed by ATC",
                "Only when the aircraft is flying within controlled airspace",
                "Regardless of ATC instructions"
            ],
            "correct": "Unless otherwise directed by ATC"
        },
        {
            "question": "The Vertical Separation Minimum (VSM) for flights in accordance with IFR within controlled airspace below FL290 is:",
            "choices": ["500 feet (150m)", "2500 feet (750 m)", "1000 feet (300m)", "2000 feet (600m)"],
            "correct": "1000 feet (300m)"
        },
        {
            "question": "An aircraft is converging from the left. Which light will you see first?",
            "choices": ["Red", "Green", "Blue", "White"],
            "correct": "Red"
        },
        {
            "question": "What minimum ground visibility is required to enable a SVFR flight to take off from an aerodrome in a CTR?",
            "choices": ["1000m", "1500m", "2000m", "3000m"],
            "correct": "1500m"
        },
        {
            "question": "If so equipped, when should an aircraft display the anti-collision light?",
            "choices": [
                "Only at night in flight, but not on the ground if being towed",
                "Whilst taxiing but not whilst being towed",
                "Only at night with engines running",
                "At all times on the ground when the engines are running"
            ],
            "correct": "At all times on the ground when the engines are running"
        },
        {
            "question": "The loading limitations shall include:",
            "choices": [
                "All limiting mass and centre of gravity",
                "All limiting mass, centre of gravity position, mass distribution and floor loading",
                "All limiting mass, centre of gravity position and floor loading",
                "All limiting mass, mass distributions and centre of gravity"
            ],
            "correct": "All limiting mass, centre of gravity position and floor loading"
        },
        {
            "question": "Aircraft A flies in VMC with an ATC clearance within a control area. Aircraft B without ATC clearance approaches at roughly the same height on a converging heading. Who has the right of way?",
            "choices": [
                "Aircraft A, regardless of the direction from which B approaches",
                "Aircraft B, regardless of the direction from which A approaches",
                "Aircraft A, if B is to the right of him",
                "Aircraft B, if A is to the left of him"
            ],
            "correct": "Aircraft B, if A is to the left of him"
        },
        {
            "question": "When a state renders valid a license issued by another Contracting State, as an alternative to issuance of its own license, the validity shall:",
            "choices": [
                "Not extend beyond 15 days after the validity of the license",
                "Not extend beyond the period of validity of the license",
                "Be at the discretion of the Contracting State rendering it valid",
                "Be at the discretion of ICAO"
            ],
            "correct": "Not extend beyond the period of validity of the license"
        },
        {
            "question": "The International Civil Aviation Organisation (ICAO) establishes:",
            "choices": [
                "Standards and recommended international practices for contracting member states",
                "Aeronautical standards adopted by all states",
                "Proposals for aeronautical regulations in the form of 18 annexes",
                "Standards and recommended practices applied without exception by all states, signatory to the Chicago convention"
            ],
            "correct": "Standards and recommended international practices for contracting member states"
        },
        {
            "question": "Which of the following is an obligation of being an ICAO contracting state?",
            "choices": [
                "ICAO must be informed about all new flight crew licenses and any suspended validity of such licenses",
                "ICAO must be informed about differences from the standards detailed in any of the annexes to the Chicago convention",
                "ICAO must approve the pricing of tickets on international airline connections",
                "ICAO must be informed about changes to national regulations"
            ],
            "correct": "ICAO must be informed about differences from the standards detailed in any of the annexes to the Chicago convention"
        },
        {
            "question": "What is the minimum vertical separation between IFR flights flying in the same direction below FL 290?",
            "choices": ["500ft", "1000ft", "2000ft", "4000ft"],
            "correct": "1000ft"
        },
        {
            "question": "During a straight departure, the initial track is to be:",
            "choices": [
                "Within 5° of runway centre-line",
                "Within 10° of runway centre-line",
                "Within 15° of runway centre-line",
                "Within 25° of runway centre-line"
            ],
            "correct": "Within 15° of runway centre-line"
        },
        {
            "question": "When given instructions to set a mode/code, a pilot shall:",
            "choices": [
                "Only use the word 'wilco'",
                "Only read back the code",
                "Only use the word 'roger'",
                "Read back mode and code"
            ],
            "correct": "Read back mode and code"
        },
        {
            "question": "The transition of altitude to flight level and vice versa is made:",
            "choices": [
                "On the transition level in the climb and transition altitude in the descent",
                "At the transition altitude in the climb and transition level in the descent",
                "At the transition level only",
                "At the transition altitude only"
            ],
            "correct": "At the transition altitude in the climb and transition level in the descent"
        },
        {
            "question": "When an aircraft subjected to unlawful interference has landed in a Contracting State, it shall notify by the most expeditious means the State of Registry and the State of the Operator of the landing and, in addition, shall similarly transmit all other relevant information to:",
            "choices": [
                "Each State whose citizens suffered fatalities or injuries, each State whose citizens were detained as hostages, each State whose citizens were known to be on board and ICAO",
                "ICAO only",
                "Each State whose citizens were known to be on board only",
                "ICAO and each State whose citizens were known to be on board only"
            ],
            "correct": "Each State whose citizens suffered fatalities or injuries, each State whose citizens were detained as hostages, each State whose citizens were known to be on board and ICAO"
        },
        {
            "question": "The emergency lights on a passenger-carrying airplane must be armed or turned on during:",
            "choices": [
                "Takeoff and landing only",
                "Taxiing, takeoff and landing",
                "Flight conditions above FL100"
            ],
            "correct": "taxiing, takeoff and landing"
        },
        {
            "question": "If a turbine-engine powered, pressurized airplane is not equipped with quick-donning oxygen masks, what is the maximum flight altitude authorized without one pilot wearing and using an oxygen mask?",
            "choices": ["Flight Level 180", "Flight Level 250", "Flight Level 350"],
            "correct": "Flight Level 250"
        },

        # --- Flashcard Section ---
        {
            "question": "What is the distinction between an ATC distress message and an urgency message?",
            "choices": [],
            "correct": "There is grave and imminent danger which requires immediate assistance"
        },
        {
            "question": "Which aircraft type has final operational priority to land over any other traffic?",
            "choices": [],
            "correct": "An emergency"
        },
        {
            "question": "What does a double white cross displayed inside an aerodrome signal square signify?",
            "choices": [],
            "correct": "Glider flying in progress"
        },
        {
            "question": "The transition from IFR flight rules to VFR flight rules is performed exclusively on whose authority?",
            "choices": [],
            "correct": "On the Captain's initiative"
        },
        {
            "question": "Pilots are strictly prohibited from using the transponder Ident function unless what condition is met?",
            "choices": [],
            "correct": "If asked by ATC"
        },
        {
            "question": "What identifier is used in Box 16 of the ICAO Flight Plan if an aerodrome has no assigned ICAO locator?",
            "choices": [],
            "correct": "ZZZZ"
        },
        {
            "question": "What does a series of red flashes from an airport control tower indicate to an aircraft flying in the visual circuit?",
            "choices": [],
            "correct": "Do not land because the aerodrome is unusable"
        },
        {
            "question": "What signal is used by an aircraft in the traffic pattern that suffers a radio failure to indicate difficulties compelling it to land without immediate assistance?",
            "choices": [],
            "correct": "The repeated switching on and off of the landing lights"
        },
        {
            "question": "What radius distance from a navigation facility does the Minimum Sector Altitude (MSA) provide obstacle clearance for?",
            "choices": [],
            "correct": "25nm"
        },
        {
            "question": "What target safety clearance does the MSA provide over obstacles inside its defined radius?",
            "choices": [],
            "correct": "300m (1,000 feet)"
        },
        {
            "question": "What does a marshaller signal indicating crossed hands in front of the face with palms outward moving arms outward represent?",
            "choices": [],
            "correct": "Remove chocks"
        },
        {
            "question": "Who retains absolute final authority as to the disposition and operation of the aircraft during flight?",
            "choices": [],
            "correct": "The Commander"
        },
        {
            "question": "What aircraft category boundary applies to an explicit Type Rating requirement?",
            "choices": [],
            "correct": "An aircraft that requires multi-pilot operation"
        },
        {
            "question": "What target message definition corresponds to an intercepted aircraft performing an abrupt breakaway climbing turn of 90 degrees or more without crossing the interceptor's track?",
            "choices": [],
            "correct": "You may proceed"
        },
        {
            "question": "What is the training requirement definition for flight crewmembers who have not qualified and served in the same capacity on another airplane of the same tech group?",
            "choices": [],
            "correct": "initial training"
        },
        {
            "question": "A crewmember who has served as second-in-command on a type may serve as pilot-in-command upon completing which program?",
            "choices": [],
            "correct": "upgrade training"
        },
        {
            "question": "How many portable battery-powered megaphones are required on an air carrier cabin configured with a seating capacity of 100 passengers?",
            "choices": [],
            "correct": "Two megaphones (one installed at the forward end and the other at the rearward location)"
        },
        {
            "question": "What is the minimum number of flight attendants required on an airplane with a passenger seating capacity of 188 with only 117 passengers aboard?",
            "choices": [],
            "correct": "four"
        },
        {
            "question": "What flight phases are included under the strict definition of 'critical phase of flight'?",
            "choices": [],
            "correct": "Taxi, takeoff, landing, and all other operations conducted below 10,000 feet, excluding cruise flight"
        },
        {
            "question": "If an engine's rotation is completely stopped in flight, who must the PIC report this to as soon as practicable?",
            "choices": [],
            "correct": "appropriate ground radio station"
        },
        {
            "question": "What operational step must the PIC take if one engine on a twin-engine air carrier airplane fails or is shut down?",
            "choices": [],
            "correct": "Land at the nearest suitable airport in point of time at which a safe landing can be made"
        },
        {
            "question": "What total flight hour experience must an applicant for an ATPL (A) have logged, and what maximum can be completed in a simulator?",
            "choices": [],
            "correct": "1500 hours total, with a maximum of 100 hours completed in a simulator"
        },
        {
            "question": "What are the horizontal distance criteria for an extended over-water operation utilizing aircraft with a MTOW greater than 5,700kg?",
            "choices": [],
            "correct": "More than 400NM from the nearest shoreline or a distance covered in 120 minutes of flight"
        },
        {
            "question": "What are the horizontal distance criteria for an extended over-water operation utilizing aircraft with a MTOW less than 5,700kg?",
            "choices": [],
            "correct": "More than 100NM from the nearest shoreline or a distance covered in 30 minutes of flight"
        },
        {
            "question": "What is the minimum recent experience requirement for a pilot to act as PIC or co-pilot of a civil aircraft under commercial transport?",
            "choices": [],
            "correct": "Within the preceding 90 days, the pilot has made at least 3 takeoffs and landings in an aircraft of the same type or approved simulator"
        },
        {
            "question": "What currency timeline conditions apply to a pilot maintaining IFR or IMC privileges?",
            "choices": [],
            "correct": "Logged at least 6 hours of instrument flight and completed at least 6 instrument approaches within the past 6 calendar months"
        },
        {
            "question": "What alcohol restriction applies to crew members prior to executing duty operations?",
            "choices": [],
            "correct": "No person may act or attempt to act as a crew member within 8 hours after consumption of any alcoholic beverage"
        },
        {
            "question": "What flashlight requirement applies to crew members operating night sequences?",
            "choices": [],
            "correct": "Each crew member involved in night operations shall have a flashlight in good working order at his or her station"
        },
        {
            "question": "What is the daytime reserve fuel requirement for a turbojet airplane operating under VFR rules?",
            "choices": [],
            "correct": "Enough fuel to fly to the first point of intended landing, plus at least 30 minutes thereafter at normal cruise"
        },
        {
            "question": "What is the reserve fuel supply requirement for a domestic air carrier operating IFR?",
            "choices": [],
            "correct": "45 minutes at normal fuel consumption in addition to fuel required to fly to the most distant alternate"
        },
        {
            "question": "What is the maximum scheduling flight time limitation allowed for a flag carrier pilot operating a two-pilot crew within any 24 consecutive hours?",
            "choices": [],
            "correct": "8 hours"
        },
        {
            "question": "What is the maximum cumulative flying hour limit for a supplemental air carrier pilot within any 30 consecutive days?",
            "choices": [],
            "correct": "100 hours"
        },
        {
            "question": "What is the required line check interval for a domestic air carrier PIC?",
            "choices": [],
            "correct": "Required every 12 calendar months in one of the types of airplane flown"
        },
        {
            "question": "A flight crewmember must be able to don and use a quick-donning oxygen mask within what maximum timeframe?",
            "choices": [],
            "correct": "5 seconds"
        },
        {
            "question": "If a pilot is responsible for an operational deviation during an emergency, within how many days must a written report be submitted?",
            "choices": [],
            "correct": "10 days after returning to home base"
        },
        {
            "question": "Name the primary topic handled by PCAR Part 1.",
            "choices": [],
            "correct": "General Policies, Procedures and Definitions"
        },
        {
            "question": "Name the primary topic handled by PCAR Part 2.",
            "choices": [],
            "correct": "Personnel Licensing"
        },
        {
            "question": "Name the primary topic handled by PCAR Part 7.",
            "choices": [],
            "correct": "Instruments and Equipment"
        },
        {
            "question": "Name the primary topic handled by PCAR Part 8.",
            "choices": [],
            "correct": "Operations"
        },
        {
            "question": "What is the license suspension sanction range for a pilot who takes off in an overloaded aircraft?",
            "choices": [],
            "correct": "60 to 120 days suspension"
        },
        {
            "question": "What is the license suspension sanction range for a pilot found guilty of flight fuel mismanagement?",
            "choices": [],
            "correct": "30 to 150 days suspension"
        },
        {
            "question": "What is the license suspension sanction range for executing a taxi, takeoff, or landing without a clearance where an ATC tower is in operation?",
            "choices": [],
            "correct": "30 to 90 days suspension"
        }
    ],
    "Meteorology": [
        # --- Multiple Choice Section ---
        {
            "question": "What is the relationship between QFE and QNH at an airport 50ft below MSL?",
            "choices": ["QFE = QNH", "QFE < QNH", "QFE > QNH", "There is no clear relationship"],
            "correct": "QFE > QNH"
        },
        {
            "question": "Which cloud type may indicate the presence of severe turbulence?",
            "choices": ["Cirrocumulus", "Nimbostratus", "Altocumulus lenticularis", "Stratocumulus"],
            "correct": "Altocumulus lenticularis"
        },
        {
            "question": "What causes wind?",
            "choices": ["Difference in pressure", "Rotation of the earth", "Frontal systems", "Difference in temperature"],
            "correct": "Difference in pressure"
        },
        {
            "question": "In what cloud is icing and turbulence most severe?",
            "choices": ["Cb", "Ns", "Sc", "Ci"],
            "correct": "Cb"
        },
        {
            "question": "Which cloud would you encounter the most intensive rain?",
            "choices": ["Ci", "Ns", "St", "Sc"],
            "correct": "Ns"
        },
        {
            "question": "How do you calculate the lowest usable flight level?",
            "choices": ["Lowest QNH and lowest negative temperature below ISA", "Lowest QNH and highest negative temperature below ISA", "Highest QNH and highest temperature above ISA", "Highest QNH and lowest temperature"],
            "correct": "Lowest QNH and lowest negative temperature below ISA"
        },
        {
            "question": "The most dangerous form of airframe icing is:",
            "choices": ["Clear ice", "Hoar frost", "Dry ice", "Rime ice"],
            "correct": "Clear ice"
        },
        {
            "question": "Generally, as altitude increases:",
            "choices": ["Temperature decreases and density increases", "Temperature, pressure and density decreases", "Temperature and pressure increase and density decreases", "Temperature decreases and pressure and density increase"],
            "correct": "Temperature, pressure and density decreases"
        },
        {
            "question": "Where is wind shear the greatest?",
            "choices": ["Near a strong low level inversion and in the region of a thunderstorm", "Near a valley with wind speeds greater than 35kts", "On the windward side of a mountain", "When the wind is greater than 35kts"],
            "correct": "Near a strong low level inversion and in the region of a thunderstorm"
        },
        {
            "question": "Where do you find the majority of the air within the atmosphere?",
            "choices": ["Troposphere", "Stratosphere", "Tropopause", "Mesosphere"],
            "correct": "Troposphere"
        },
        {
            "question": "Where is the 300mb level approximately in ISA?",
            "choices": ["30,000ft", "39,000ft", "18,000ft", "10,000ft"],
            "correct": "30,000ft"
        },
        {
            "question": "What type of precipitation would you expect at an active unstable cold front?",
            "choices": ["Freezing rain", "Light to moderate continuous rain", "Drizzle", "Showers associated with thunderstorms"],
            "correct": "Showers associated with thunderstorms"
        },
        {
            "question": "Where are icing conditions on route specified?",
            "choices": ["TAF and METAR", "METAR and SIGMET", "SWC (sig. weather chart) and SIGMET", "SPECI and TREND"],
            "correct": "SWC (sig. weather chart) and SIGMET"
        },
        {
            "question": "You are flying at FL170. The pressure level which is closest to you is the:",
            "choices": ["300mb", "700mb", "500mb", "850mb"],
            "correct": "500mb"
        },
        {
            "question": "In which weather report would you expect to find information about icing conditions on the runway?",
            "choices": ["GAFOR", "TAF", "METAR", "SIGMET"],
            "correct": "METAR"
        },
        {
            "question": "TAFs are usually valid for:",
            "choices": ["For the period indicated in the TAF itself", "For 18 hours", "For 24 hours", "For 8 hours"],
            "correct": "For the period indicated in the TAF itself"
        },
        {
            "question": "When a TREND is included at the end of a METAR, the trend is a forecast valid for:",
            "choices": ["1 hour after the time of observation", "2 hours after the time of observation", "2 hours after it was issued", "1 hour after it was issued"],
            "correct": "2 hours after the time of observation"
        },
        {
            "question": "VOLMETs are updated:",
            "choices": ["Every hour", "4 times a day", "2 times a day", "Every half hour"],
            "correct": "Every half hour"
        },
        {
            "question": "QFE is 1000 hPa with an airfield elevation of 200m AMSL. What is QNH? (use 8m per hPa)",
            "choices": ["975 hPa", "1025 hPa", "1008 hPa", "992 hPa"],
            "correct": "1025 hPa"
        },
        {
            "question": "What is normally the most effective measure to reduce or avoid CAT effects?",
            "choices": ["Change of flight level", "Change of course", "Increase of speed", "Decrease of speed"],
            "correct": "Change of flight level"
        },
        {
            "question": "An inversion is:",
            "choices": ["A decrease of pressure with height", "A decrease of temperature with height", "An increase of temperature with height", "An increase of pressure with height"],
            "correct": "An increase of temperature with height"
        },
        {
            "question": "The isobars drawn on a surface weather chart represent lines of equal pressure:",
            "choices": ["At flight level", "At height of observatory", "At a determined density altitude", "Reduced to sea level"],
            "correct": "Reduced to sea level"
        },
        {
            "question": "How does a pilot react to heavy freezing rain at 2,000ft/AGL, when he is unable to deice nor land?",
            "choices": ["He ascends to the cold air layer above", "He continues to fly at the same altitude", "He turns back before the aircraft loses maneuverability", "He descends to the warm air layer below"],
            "correct": "He turns back before the aircraft loses maneuverability"
        },
        {
            "question": "Two aircrafts, one with a sharp wing profile (S) and the other with a thick profile (T), are flying through the same cloud with the same true airspeed. The cloud consists of small supercooled droplets. Which statement is correct concerning ice accretion?",
            "choices": ["Aircraft T experiences more icing than S", "Aircraft S and T experience the same amount of icing", "Neither of the aircrafts accumulate ice due to the small size of droplets", "Aircraft S experiences more icing than T"],
            "correct": "Aircraft S experiences more icing than T"
        },
        {
            "question": "ATC will only report wind as gusting if:",
            "choices": ["Gust speed exceeds mean speed by >15kts", "Gusts to over 25kts", "Gusts exceed mean speed by 10kts", "Gusts to under 25kts"],
            "correct": "Gust speed exceeds mean speed by >15kts"
        },
        {
            "question": "A flight is to depart from an airport with runway 09 and 27. Surface wind is 270/05; an inversion is reported at 300 feet with turbulence and wind shear. The wind just above the inversion is 090/30. What is the safest departure procedure?",
            "choices": ["Take-off is not possible under these conditions", "Depart on runway 09 with a tailwind", "Depart runway 27 with maximum throttle during the passage through the inversion", "Depart runway 27 with as steep an ascent as possible"],
            "correct": "Depart on runway 09 with a tailwind"
        },
        {
            "question": "You are cruising at FL 200, OAT is -40°C, sea level pressure is 1033 hPa. Calculate the true altitude.",
            "choices": ["20,660 ft", "21,740 ft", "18,260 ft", "19, 340 ft"],
            "correct": "18,260 ft"
        },
        {
            "question": "In what frequency band is the ATIS normally broadcasted?",
            "choices": ["LF", "HF", "ADF", "VHF"],
            "correct": "VHF"
        },
        {
            "question": "Which constant pressure altitude chart is standard for a 30,065 ft pressure level (FL 300)?",
            "choices": ["200 hPa", "700 hPa", "500 hPa", "300 hPa"],
            "correct": "300 hPa"
        },
        {
            "question": "With regard to RVR and Met vis:",
            "choices": ["Met vis is usually less than RVR", "Met vis is usually greater than RVR", "RVR is usually less than met vis", "Met vis and RVR are usually the same"],
            "correct": "Met vis is usually less than RVR"
        },
        {
            "question": "The station pressure used in surface weather charts is:",
            "choices": ["QNE", "QFF", "QFE", "QNH"],
            "correct": "QFF"
        },
        {
            "question": "What is the coldest time of the day?",
            "choices": ["1hr before sunrise", "1/2 hr before sunrise", "At exact moment of sunrise", "1/2 hour after sunrise"],
            "correct": "1/2 hour after sunrise"
        },
        {
            "question": "The code 'BECMG FM 1100 -RASH' in a METAR means:",
            "choices": ["From 1100UTC, the cessation of rain showers", "Becoming from 1100UTC slight rain showers", "Becoming from 1100UTC rain showers", "Becoming from 1100UTC till 0000UTC slight rain showers"],
            "correct": "Becoming from 1100UTC slight rain showers"
        },
        {
            "question": "Which of the following statements is a correct interpretation of the METAR entry: 00000KT 0200 R14/0800U R16/P1500U FZFG VV001 m03/m03 Q1022 BECMG 0800?",
            "choices": [
                "Meteorological visibility 200m, RVR for runway 16 1500m, temperature -3°C, vertical visibility 100m",
                "Meteorological visibility 200ft, RVR for runway 16 more than 1500m, vertical visibility 100ft, fog with hoar frost",
                "Meteorological visibility for runway 14 800m, fog with hoar frost, RVR for runway 16 more than 1500m",
                "RVR for runway 14 800m, vertical visibility 100ft, calm, meteorological visibility improving to 800m in the next 2 hours"
            ],
            "correct": "RVR for runway 14 800m, vertical visibility 100ft, calm, meteorological visibility improving to 800m in the next 2 hours"
        },
        {
            "question": "Refer to the following TAF for Zurich: LSZH 261019 20018G30KT 9999 -RA SCT050 BKN080 TEMPO 23012KT 6000 -DZ BKN015 BKN030 BECMG 1518 23020G35KT 4000 RA OVC010=. The lowest visibility forecast at ETA Zurich 1430 UTC is:",
            "choices": ["6km", "6nm", "4km", "10km"],
            "correct": "6km"
        },
        {
            "question": "Which of the following statements is a correct interpretation of the SIGMET: LSAW SWITZERLAND 0307 SIGMET 2 VALID 030700/031100 LSSW mod to sev cat fcst north of alps btn fl 260 and fl 380 / stnr / intsf = ?",
            "choices": [
                "Severe turbulence observed below FL 260 north of the Alps. Pilots advised to cross this area above FL 380",
                "Moderate to strong clear air turbulence of constant intensity to be expected north of the Alps",
                "Moderate to severe clear air turbulence to be expected north of the Alps. Intensity increasing. Danger zone between FL260 and FL380",
                "Zone of moderate to severe turbulence moving towards the area north of the Alps. Intensity increasing. Pilots advised to cross this area above FL260"
            ],
            "correct": "Moderate to severe clear air turbulence to be expected north of the Alps. Intensity increasing. Danger zone between FL260 and FL380"
        },
        {
            "question": "From a pre-flight briefing you know a jet stream is at 31,000ft whilst you are at FL270. You experience moderate CAT. What would be the best course of action?",
            "choices": ["Stay level", "Descend", "Climb", "Reduce speed"],
            "correct": "Descend"
        },
        {
            "question": "In which zone of a jetstream is the strongest CAT to be expected?",
            "choices": ["The warm air side of the core", "Exactly in the center of the core", "About 12,000ft above the core", "The cold air side of the core"],
            "correct": "The cold air side of the core"
        },
        {
            "question": "In an area of converging air:",
            "choices": ["Clouds cannot be formed", "Clouds can be formed", "Convective clouds can be dissolved", "Stratified clouds can be dissolved"],
            "correct": "Clouds can be formed"
        },
        {
            "question": "The greater the pressure gradient the:",
            "choices": ["Closer the isobars and the lower the temperatures", "Further the isobars will be apart and the higher the temperature", "Closer the isobars and the stronger the wind", "Further the isobars will be apart and the weaker the wind"],
            "correct": "Closer the isobars and the stronger the wind"
        },
        {
            "question": "Under what condition is pressure altitude and density altitude the same value?",
            "choices": ["At standard temperature.", "When indicated, and pressure sure altitudes are the same value on the altimeter.", "When the altimeter setting is 29.92\" Hg."],
            "correct": "At standard temperature."
        },
        {
            "question": "Under which condition will pressure altitude be equal to true altitude?",
            "choices": ["When standard atmospheric conditions exist.", "When the atmospheric pressure is 29.92\" Hg.", "When indicated altitude is equal to the pressure altitude."],
            "correct": "When standard atmospheric conditions exist."
        },
        {
            "question": "Which condition would cause the altimeter to indicate a lower altitude than actually flown (true altitude)?",
            "choices": ["Air temperature lower than standard.", "Air temperature warmer than standard.", "Atmospheric pressure lower than standard."],
            "correct": "Air temperature warmer than standard."
        },
        {
            "question": "Which is true regarding the use of airborne weather-avoidance radar for the recognition of certain weather conditions?",
            "choices": [
                "The avoidance of hail is assured when flying between and just clear of the most intense echoes.",
                "The radarscope provides no assurance of avoiding instrument weather conditions.",
                "The clear area between intense echoes indicates that visual sighting of storms can be maintained when flying between the echoes."
            ],
            "correct": "The radarscope provides no assurance of avoiding instrument weather conditions."
        },
        {
            "question": "When an altimeter is changed from 30.11\" Hg to 29.96\" Hg, in which direction will the indicated altitude change and by what value?",
            "choices": ["Altimeter will indicate 150 feet higher.", "Altimeter will indicate 150 feet lower.", "Altimeter will indicate 15 feet lower."],
            "correct": "Altimeter will indicate 150 feet lower."
        },
        {
            "question": "A common type of ground or surface based temperature inversion is that which is produced by:",
            "choices": [
                "ground radiation on clear, cool nights when the wind is light.",
                "warm air being lifted rapidly aloft in the vicinity of mountainous terrain.",
                "the movement of colder air over warm air, or the movement of warm air under cold air."
            ],
            "correct": "ground radiation on clear, cool nights when the wind is light."
        },
        {
            "question": "How much colder than standard temperature is the forecast temperature at 9,000 feet, as indicated by an excerpt showing standard vs forecast (e.g., 0737-04 vs 1043-10)?",
            "choices": ["7°C.", "10 °C.", "3°C"],
            "correct": "7°C."
        },
        {
            "question": "The primary cause of all changes in the Earth's weather is:",
            "choices": ["changes in air pressure over the Earth's surface.", "movement of the air masses.", "variation of solar energy received by the Earth's regions."],
            "correct": "variation of solar energy received by the Earth's regions."
        },
        {
            "question": "A characteristic of the stratosphere is:",
            "choices": ["a relatively even base altitude of approximately 35,000 feet.", "relatively small changes in temperature with an increase in altitude.", "an overall decrease of temperature with an increase in altitude."],
            "correct": "relatively small changes in temperature with an increase in altitude."
        },
        {
            "question": "Steady precipitation, in contrast to showers, preceding a front is an indication of:",
            "choices": ["stratiform clouds with moderate turbulence.", "stratiform clouds with little or no turbulence.", "cummuliform clouds with little or no turbulence."],
            "correct": "stratiform clouds with little or no turbulence."
        },
        {
            "question": "The presence of ice pellets at the surface is evidence that:",
            "choices": ["there is freezing rain at a higher altitude.", "there are thunderstorms in the area.", "a cold front has passed."],
            "correct": "there is freezing rain at a higher altitude."
        },
        {
            "question": "Which conditions result in the formation of frost?",
            "choices": [
                "Temperature of the collecting surface is below the dewpoint of surrounding air and the dewpoint is colder than freezing.",
                "When dew forms and the temperature is below freezing.",
                "The temperature of the collecting surface is at or below freezing and small droplets of moisture are falling."
            ],
            "correct": "Temperature of the collecting surface is below the dewpoint of surrounding air and the dewpoint is colder than freezing."
        },
        {
            "question": "Under what condition will true altitude be lower than indicated altitude with an altimeter setting of 29.92\" Hg?",
            "choices": ["In warmer than standard air temperature.", "When density altitude is higher than indicated altitude.", "In colder than standard air temperature."],
            "correct": "In colder than standard air temperature."
        },
        {
            "question": "Which of the following defines the type of altitude used when maintaining FL 210?",
            "choices": ["Pressure.", "Calibrated.", "Indicated."],
            "correct": "Pressure."
        },
        {
            "question": "If the air temperature is +8°C at an elevation of 1,350 feet and a standard temperature lapse rate exists, what will be the approximate freezing level?",
            "choices": ["5,350 feet MSL.", "3,350 feet MSL.", "9,350 feet MSL."],
            "correct": "5,350 feet MSL."
        },
        {
            "question": "What feature is associated with a temperature inversion?",
            "choices": ["Air mass thunderstorms.", "An unstable layer of air.", "A stable layer of air."],
            "correct": "A stable layer of air."
        },
        {
            "question": "What type of clouds will be formed if very stable moist air is forced upslope?",
            "choices": ["Stratified clouds with little vertical development.", "First stratified clouds and then vertical clouds.", "Vertical clouds with increasing height."],
            "correct": "Stratified clouds with little vertical development."
        },
        {
            "question": "The general characteristics of unstable air are:",
            "choices": ["good visibility, steady precipitation, and stratiform type clouds.", "poor visibility, intermittent precipitation, and cumuliform type clouds.", "good visibility, showery precipitation, and cumuliform type clouds."],
            "correct": "good visibility, showery precipitation, and cumuliform type clouds."
        },
        {
            "question": "Which is a characteristic of stable air?",
            "choices": ["Stratiform clouds.", "Unlimited visibility.", "Fair weather cumulus clouds."],
            "correct": "Stratiform clouds."
        },
        {
            "question": "What type clouds can be expected when an unstable air mass is forced to ascend a mountain slope?",
            "choices": ["Stratified clouds with considerable associated turbulence.", "Clouds with extensive vertical development.", "Layered clouds with little vertical development."],
            "correct": "Clouds with extensive vertical development."
        },
        {
            "question": "What are the characteristics of stable air?",
            "choices": ["Good visibility, steady precipitation, and stratus type clouds.", "Poor visibility, intermittent precipitation, and cumulus-type clouds.", "Poor visibility, steady precipitation, and stratus type clouds."],
            "correct": "Poor visibility, steady precipitation, and stratus type clouds."
        },
        {
            "question": "What are some characteristics of unstable air?",
            "choices": ["Turbulence and poor surface visibility.", "Turbulence and good surface visibility.", "Nimbostratus clouds and good surface visibility."],
            "correct": "Turbulence and good surface visibility."
        },
        {
            "question": "Stability can be determined from which measurement of the atmosphere?",
            "choices": ["Low level winds.", "Atmospheric pressure.", "Ambient lapse rate."],
            "correct": "Ambient lapse rate."
        },
        {
            "question": "What determines the structure or type of clouds which form as a result of air being forced to ascend?",
            "choices": ["The amount of condensation nuclei present after lifting occurs.", "The stability of the air before lifting occurs.", "The method by which the air is lifted."],
            "correct": "The stability of the air before lifting occurs."
        },
        {
            "question": "Which combination of weather producing variables would likely result in cumuliform type clouds, good visibility, rain showers, and clear type icing?",
            "choices": ["Stable, dry air, and orographic lifting.", "Unstable, moist air, and orographic lifting.", "Unstable, moist air, and no lifting mechanism."],
            "correct": "Unstable, moist air, and orographic lifting."
        },
        {
            "question": "Unsaturated air flowing upslope will cool at the dry adiabatic lapse rate of approximately:",
            "choices": ["2.5°C per 1,000 feet.", "2°C per 1,000 feet.", "3°C per 1,000 feet."],
            "correct": "3°C per 1,000 feet."
        },
        {
            "question": "Which weather phenomenon signals the beginning of the mature stage of a thunderstorm?",
            "choices": ["Strong turbulence in the cloud.", "The start of rain at the surface.", "Growth rate of cloud is maximum."],
            "correct": "The start of rain at the surface."
        },
        {
            "question": "Frontal waves normally form on:",
            "choices": ["rapidly moving cold fronts or warm fronts.", "slow moving warm fronts and strong occluded fronts.", "slow moving cold fronts or stationary fronts."],
            "correct": "slow moving cold fronts or stationary fronts."
        },
        {
            "question": "Which are characteristics of an unstable cold air mass moving over a warm surface?",
            "choices": ["Cumuliform clouds, turbulence, and good visibility.", "Stratiform clouds, smooth air, and poor visibility.", "Cumuliform clouds, turbulence, and poor visibility."],
            "correct": "Cumuliform clouds, turbulence, and good visibility."
        },
        {
            "question": "Which clouds have the greatest turbulence?",
            "choices": ["Cumulonimbus.", "Towering cumulus.", "Altocumulus castellanus."],
            "correct": "Cumulonimbus."
        },
        {
            "question": "Standing lenticular clouds, in mountainous areas, indicate:",
            "choices": ["turbulence.", "an inversion.", "unstable air."],
            "correct": "turbulence."
        },
        {
            "question": "The suffix 'nimbus', used in naming clouds, means a:",
            "choices": ["dark massive, towering cloud.", "cloud with extensive vertical development.", "raincloud."],
            "correct": "raincloud."
        },
        {
            "question": "The presence of standing lenticular altocumulus clouds is a good indication of:",
            "choices": ["heavy icing conditions.", "a jetstream.", "very strong turbulence."],
            "correct": "very strong turbulence."
        },
        {
            "question": "Which family of clouds is least likely to contribute to structural icing on an aircraft?",
            "choices": ["Low clouds.", "Clouds with extensive vertical development.", "High clouds."],
            "correct": "High clouds."
        },
        {
            "question": "What are the four families of clouds?",
            "choices": ["Stratus, cumulus, nimbus, and cirrus.", "Clouds formed by updrafts, fronts, cooling layers of air, and precipitation.", "High, middle, low, and those with extensive vertical development."],
            "correct": "High, middle, low, and those with extensive vertical development."
        },
        {
            "question": "Where can wind shear associated with a thunderstorm be found?",
            "choices": ["On all sides of the thunderstorm cell and directly under the cell.", "In front of the thunderstorm cell and directly under the cell.", "In front of the thunderstorm cell (anvil side) and on the right side of the cell."],
            "correct": "On all sides of the thunderstorm cell and directly under the cell."
        },
        {
            "question": "Which weather phenomenon is always associated with the passage of a frontal system?",
            "choices": ["A wind change.", "Clouds, either ahead or behind the front.", "An abrupt decrease in pressure."],
            "correct": "A wind change."
        },
        {
            "question": "Where do squall lines most often develop?",
            "choices": ["Ahead of a cold front.", "In a cold air mass.", "In an occluded front."],
            "correct": "Ahead of a cold front."
        },
        {
            "question": "Where does wind shear occur?",
            "choices": ["Wherever there is an abrupt decrease in pressure and/or temperature.", "With either a wind shift or a windspeed gradient at any level in the atmosphere.", "Exclusively in thunderstorms."],
            "correct": "With either a wind shift or a windspeed gradient at any level in the atmosphere."
        },
        {
            "question": "Which is a characteristic of low level wind shear as it relates to frontal activity?",
            "choices": ["With a warm front, the most critical period is before the front passes the airport.", "Turbulence will always exist in wind shear conditions.", "With a cold front, the most critical period is just before the front passes the airport."],
            "correct": "With a warm front, the most critical period is before the front passes the airport."
        },
        {
            "question": "What is indicated by the term 'embedded thunderstorms'?",
            "choices": ["Thunderstorms are obscured by massive cloud layers and cannot be seen.", "Severe thunderstorms are embedded within a squall line.", "Thunderstorms are predicted to develop in a stable air mass."],
            "correct": "Thunderstorms are obscured by massive cloud layers and cannot be seen."
        },
        {
            "question": "During the life cycle of a thunderstorm, which stage is characterized predominately by downdrafts?",
            "choices": ["Cumulus.", "Dissipating.", "Mature."],
            "correct": "Dissipating."
        },
        {
            "question": "Which weather phenomenon is always associated with a thunderstorm?",
            "choices": ["Lightning.", "Supercooled raindrops.", "Heavy rain showers."],
            "correct": "Lightning."
        },
        {
            "question": "Which thunderstorms generally produce the most severe conditions, such as heavy hail and destructive winds?",
            "choices": ["Warm front.", "Squall line.", "Air mass."],
            "correct": "Squall line."
        },
        {
            "question": "What are the requirements for the formation of a thunderstorm?",
            "choices": ["A cumulus cloud with sufficient moisture and an inverted lapse rate.", "Sufficient moisture, an unstable lapse rate, and a lifting action.", "A cumulus cloud with sufficient moisture."],
            "correct": "Sufficient moisture, an unstable lapse rate, and a lifting action."
        },
        {
            "question": "Fair weather cumulus clouds often indicate:",
            "choices": ["turbulence at and below the cloud level.", "smooth flying conditions.", "poor visibility."],
            "correct": "turbulence at and below the cloud level."
        },
        {
            "question": "Why is frost considered hazardous to flight operation?",
            "choices": ["Frost changes the basic aerodynamic shape of the airfoil.", "Frost decreases control effectiveness.", "Frost causes early airflow separation resulting in a loss of lift."],
            "correct": "Frost causes early airflow separation resulting in a loss of lift."
        },
        {
            "question": "In which meteorological environment is aircraft structural icing most likely to have the highest rate of accumulation?",
            "choices": ["Cumulonimbus clouds.", "High humidity and freezing temperature.", "Freezing rain."],
            "correct": "Freezing rain."
        },
        {
            "question": "What is an operational consideration if you fly into rain which freezes on impact?",
            "choices": ["You have flown into an area of thunderstorms.", "You have flown through a cold front.", "Temperatures are above freezing at some higher altitude."],
            "correct": "Temperatures are above freezing at some higher altitude."
        },
        {
            "question": "The average height of the troposphere in the middle latitudes is:",
            "choices": ["25,000 feet.", "37,000 feet.", "20,000 feet."],
            "correct": "37,000 feet."
        },
        {
            "question": "A jetstream is defined as wind of:",
            "choices": ["30 knots or greater.", "40 knots or greater.", "50 knots or greater."],
            "correct": "50 knots or greater."
        },
        {
            "question": "Under which condition does advection fog usually form?",
            "choices": ["Moist air moving over colder ground or water.", "Warm, moist air settling over a cool surface under no wind conditions.", "A land breeze blowing a cold air mass over a warm water current."],
            "correct": "Moist air moving over colder ground or water."
        },
        {
            "question": "A high cloud is composed mostly of:",
            "choices": ["condensation nuclei.", "ozone.", "ice crystals."],
            "correct": "ice crystals."
        },
        {
            "question": "What enhances the growth rate of precipitation?",
            "choices": ["Upward currents.", "Cyclonic movement.", "Advective action."],
            "correct": "Upward currents."
        },
        {
            "question": "If you fly into severe turbulence, which flight condition should you attempt to maintain?",
            "choices": ["Level flight attitude.", "Constant altitude and constant airspeed.", "Constant airspeed (VA)."],
            "correct": "Level flight attitude."
        },
        {
            "question": "Which precipitation type normally indicates freezing rain at higher altitudes?",
            "choices": ["Hail.", "Ice pellets.", "Snow."],
            "correct": "Ice pellets."
        },
        {
            "question": "Which weather condition can be expected when moist air flows from a relatively warm surface to a colder surface?",
            "choices": ["Fog.", "Convective turbulence due to surface heating.", "Increased visibility."],
            "correct": "Fog."
        },
        {
            "question": "Fog is usually prevalent in industrial areas because of:",
            "choices": ["atmospheric stabilization around cities.", "increased temperatures due to industrial heating.", "an abundance of condensation nuclei from combustion products."],
            "correct": "an abundance of condensation nuclei from combustion products."
        },
        {
            "question": "In what localities is advection fog most likely to occur?",
            "choices": ["Level inland areas.", "Mountain slopes.", "Coastal areas."],
            "correct": "Coastal areas."
        },
        {
            "question": "What types of fog depend upon a wind in order to exist?",
            "choices": ["Precipitation induced fog and ground fog.", "Steam fog and downslope fog.", "Advection fog and upslope fog."],
            "correct": "Advection fog and upslope fog."
        },
        {
            "question": "What situation is most conducive to the formation of radiation fog?",
            "choices": ["Moist, tropical air moving over cold, offshore water.", "The movement of cold air over much warmer water.", "Warm, moist air over low, flatland areas on clear, calm nights."],
            "correct": "Warm, moist air over low, flatland areas on clear, calm nights."
        },
        {
            "question": "The strength and location of the jetstream is normally:",
            "choices": ["stronger and farther north in the winter.", "stronger and farther north in the summer.", "weaker and farther north in the summer."],
            "correct": "weaker and farther north in the summer."
        },
        {
            "question": "The body of a Terminal Aerodrome Forecast (TAF) covers a geographical proximity within a:",
            "choices": ["15 to 20 mile radius of the center of an airport.", "10 to 15 mile radius of the center of an airport.", "5 to 10 mile radius of the center of an airport."],
            "correct": "5 to 10 mile radius of the center of an airport."
        },
        {
            "question": "What wind direction and speed is represented by the entry 9900+00 for 9,000 feet, on an Winds and Temperatures Aloft Forecast (FD)?",
            "choices": ["Light and variable; less than 5 knots.", "Vortex winds exceeding 200 knots.", "Light and variable less than 10 knots."],
            "correct": "Light and variable; less than 5 knots."
        },
        {
            "question": "What important information is provided by the Radar Summary Chart that is not shown on other weather charts?",
            "choices": ["Lines and cells of hazardous thunderstorms.", "Types of precipitation between reporting stations.", "Areas of cloud cover and icing levels within the clouds."],
            "correct": "Lines and cells of hazardous thunderstorms."
        },
        {
            "question": "What does a Convective Outlook (AC) describe for a following 24 hour period?",
            "choices": ["General thunderstorm activity.", "A severe weather watch bulletin.", "When forecast conditions are expected to continue beyond the valid period."],
            "correct": "General thunderstorm activity."
        },
        {
            "question": "Which primary source should be used to obtain forecast weather information at your destination for the planned ETA?",
            "choices": ["Radar Summary and Weather Depiction Charts.", "Terminal Aerodrome Forecast (TAF).", "Area Forecast."],
            "correct": "Terminal Aerodrome Forecast (TAF)."
        },
        {
            "question": "A calm wind entry in a Terminal Aerodrome Forecast (TAF) will be indicated when the wind is:",
            "choices": ["6 knots or less.", "9 knots or less.", "3 knots or less."],
            "correct": "3 knots or less."
        },
        {
            "question": "When the visibility is greater than 6 SM on a TAF it is expressed as:",
            "choices": ["6PSM.", "P6SM.", "6SMP."],
            "correct": "P6SM."
        },
        {
            "question": "'WND' in the categorical outlook in the Aviation Area Forecast means that the wind during that period is forecast to be:",
            "choices": ["At least 6 knots or stronger.", "At least 15 knots or stronger.", "At least 20 knots or stronger."],
            "correct": "At least 20 knots or stronger."
        },
        {
            "question": "SIGMET's are issued as a warning of weather conditions potentially hazardous:",
            "choices": ["only to light aircraft operations.", "to all aircraft.", "particularly to light aircraft."],
            "correct": "to all aircraft."
        },
        {
            "question": "Which meteorological condition is issued in the form of a SIGMET (WS)?",
            "choices": ["Moderate icing.", "Widespread sand or duststorms lowering visibility to less than 3 miles.", "Sustained winds of 30 knots or greater at the surface."],
            "correct": "Widespread sand or duststorms lowering visibility to less than 3 miles."
        },
        {
            "question": "What sources reflect the most accurate information on icing conditions (current and forecast) at the time of departure?",
            "choices": ["The Area Forecast, and the Freezing Level Chart.", "Pilot weather reports (PIREP's), AIRMET's, and SIGMET's.", "Low-Level Significant Weather Prognostic Chart, and the Area Forecast."],
            "correct": "Pilot weather reports (PIREP's), AIRMET's, and SIGMET's."
        },
        {
            "question": "What is the maximum forecast period for AIRMET's?",
            "choices": ["Six hours.", "Two hours.", "Four hours."],
            "correct": "Six hours."
        },
        {
            "question": "Decode the excerpt from the Winds and Temperature Aloft Forecast (FD) for OKC at 39,000 feet showing 'OKC 830558'.",
            "choices": ["Wind 330° at 205 knots, temperature -58°C", "Wind 330° at 105 knots, temperature -58°C.", "Wind 130° at 50 knots, temperature -58°C."],
            "correct": "Wind 330° at 105 knots, temperature -58°C."
        },
        {
            "question": "Which values are used for winds aloft forecasts?",
            "choices": ["True direction and knots.", "Magnetic direction and MPH.", "Magnetic direction and knots."],
            "correct": "True direction and knots."
        },
        {
            "question": "What flight planning information can a pilot derive from constant pressure charts?",
            "choices": ["Levels of widespread cloud coverage.", "Winds and temperatures aloft.", "Clear air turbulence and icing conditions."],
            "correct": "Winds and temperatures aloft."
        },
        {
            "question": "Which weather conditions should be expected beneath a low level temperature inversion layer when the relative humidity is high?",
            "choices": ["Smooth air and poor visibility due to fog, haze, or low clouds.", "Turbulent air and poor visibility due to fog, low stratus type clouds, and showery precipitation.", "Light wind shear and poor visibility due to haze and light rain."],
            "correct": "Smooth air and poor visibility due to fog, haze, or low clouds."
        },
        {
            "question": "A ceiling is defined as the height of the:",
            "choices": ["lowest layer of clouds that contributed to the overall overcast.", "lowest layer of clouds or obscuring phenomena aloft that is reported as broken or overcast.", "highest layer of clouds or obscuring phenomena aloft that covers over 6/10 of the sky."],
            "correct": "lowest layer of clouds or obscuring phenomena aloft that is reported as broken or overcast."
        },
        {
            "question": "A pilot reporting turbulence that momentarily causes slight, erratic changes in altitude and/or attitude should report it as:",
            "choices": ["moderate turbulence.", "light turbulence.", "light chop."],
            "correct": "light turbulence."
        },
        {
            "question": "The Low-Level Significant Weather Prognostic Chart depicts weather conditions:",
            "choices": ["as they existed at the time the chart was prepared.", "that existed at the time shown on the chart which is about 3 hours before the chart is received.", "that are forecast to exist at a valid time shown on the chart."],
            "correct": "that are forecast to exist at a valid time shown on the chart."
        },
        {
            "question": "Which primary source should you obtain information regarding the weather expected to exist at your destination at your estimated time of arrival?",
            "choices": ["Radar Summary and Weather Depiction Chart.", "Weather Depiction Chart.", "Terminal Aerodrome Forecast."],
            "correct": "Terminal Aerodrome Forecast."
        },
        {
            "question": "Hazardous wind shear is commonly encountered near the ground:",
            "choices": ["during periods when the wind velocity is stronger than 35 knots.", "during periods when the wind velocity is stronger than 35 knots and near mountain valleys.", "during periods of strong temperature inversion and near thunderstorms."],
            "correct": "during periods of strong temperature inversion and near thunderstorms."
        },
        {
            "question": "What is the expected duration of an individual microburst?",
            "choices": ["One microburst may continue for as long as 2 to 4 hours.", "Seldom longer than 15 minutes from the time the burst strikes the ground until dissipation.", "Two minutes with maximum winds lasting approximately 1 minute."],
            "correct": "Seldom longer than 15 minutes from the time the burst strikes the ground until dissipation."
        },
        {
            "question": "Maximum downdrafts in a microburst encounter may be as strong as:",
            "choices": ["8,000 feet per minute.", "7,000 feet per minute.", "6,000 feet per minute."],
            "correct": "6,000 feet per minute."
        },
        {
            "question": "An aircraft that encounters a headwind of 45 knots, within a microburst, may expect a total shear across the microburst of:",
            "choices": ["80 knots.", "90 knots.", "40 knots."],
            "correct": "90 knots."
        },
        {
            "question": "What term describes an elongated area of low pressure?",
            "choices": ["Trough.", "Ridge.", "Hurricane or typhoon."],
            "correct": "Trough."
        },
        {
            "question": "Which weather condition is defined as an anticyclone?",
            "choices": ["Calm.", "High pressure area.", "COL."],
            "correct": "High pressure area."
        },
        {
            "question": "What is the feature of air movement in high pressure area?",
            "choices": ["Ascending from the surface high to lower pressure at higher altitudes.", "Descending to the surface and then outward.", "Moving outward from the high at high altitudes and into the high at the surface."],
            "correct": "Descending to the surface and then outward."
        },
        {
            "question": "Where is the usual location of a thermal low?",
            "choices": ["Over the arctic region.", "Over the eye of a hurricane.", "Over the surface of a dry, sunny region."],
            "correct": "Over the surface of a dry, sunny region."
        },
        {
            "question": "Which event usually occurs after an aircraft passes through a front into the colder air?",
            "choices": ["Temperature/dewpoint spread decreases.", "Wind direction shifts to the left.", "Atmospheric pressure increases."],
            "correct": "Atmospheric pressure increases"
        },
        {
            "question": "What is the feature of a stationary front?",
            "choices": ["The warm front surface moves about half the speed of the cold front surface.", "Weather conditions are a combination of strong cold front and strong warm front weather.", "Surface winds tend to flow parallel to the frontal zone."],
            "correct": "Surface winds tend to flow parallel to the frontal zone."
        },
        {
            "question": "Which atmospheric factor causes rapid movement of surface fronts?",
            "choices": ["Upper winds blowing across the front.", "Upper low located directly over the surface.", "The cold front overtaking and lifting the warm front."],
            "correct": "Upper winds blowing across the front."
        },
        {
            "question": "What type weather change is to be expected in an area where frontolysis is reported?",
            "choices": ["The frontal weather is becoming stronger.", "The front is dissipating.", "The front is moving at a faster speed."],
            "correct": "The front is dissipating."
        },
        {
            "question": "What weather difference is found on each side of a 'dry line'?",
            "choices": ["Extreme temperature difference.", "Dewpoint difference.", "Status versus cumulus clouds."],
            "correct": "Dewpoint difference."
        },
        {
            "question": "At lower levels of the atmosphere, friction causes the wind to flow across isobars into a low because the friction:",
            "choices": ["Decreases windspeed and coriolis force.", "Decreases pressure gradient force.", "Creates air turbulence and raises atmospheric pressure."],
            "correct": "Decreases windspeed and coriolis force."
        },
        {
            "question": "At which location does coriolis force have the least effect on wind direction?",
            "choices": ["At the poles.", "Middle latitudes (30°-60°).", "At the equator."],
            "correct": "At the equator."
        },
        {
            "question": "How does coriolis force effect wind direction in the southern hemisphere?",
            "choices": ["Causes clockwise rotation around a low.", "Causes wind to flow out of a low toward a high.", "Has exactly the same effect as in the northern hemisphere."],
            "correct": "Causes clockwise rotation around a low."
        },
        {
            "question": "What minimum thickness of cloud layer is indicated if precipitation is reported as light or greater intensity?",
            "choices": ["4,000 feet thick.", "2,000 feet thick.", "A thickness which allows the cloud tops to be higher than the freezing level."],
            "correct": "4,000 feet thick."
        },
        {
            "question": "Which weather condition produces weather on the lee side of the lake?",
            "choices": ["Warm air flowing over a colder lake may produce fog.", "Cold air flowing over a warmer lake may produce advection for.", "Warm air flowing over a cool lake may produce rainshowers."],
            "correct": "Warm air flowing over a colder lake may produce fog."
        },
        {
            "question": "What is the lowest cloud in the stationary group associated with a mountain wave?",
            "choices": ["Rotor cloud.", "Standing lenticular.", "Low stratus."],
            "correct": "Rotor cloud."
        },
        {
            "question": "When advection fog has developed, what may tend to dissipate or lift the fog into stratus clouds?",
            "choices": ["Temperature inversion.", "Wind stronger than 15 knots.", "Surface radiation."],
            "correct": "Wind stronger than 15 knots."
        },
        {
            "question": "Which conditions are necessary for the formation of upslope fog?",
            "choices": ["Moist, stable air being moved over gradually rising ground by a wind.", "A clear sky, little or no wind, and 100% relative humidity.", "Rain falling through stratus clouds and a 10-25 knots wind moving the precipitation up the slope."],
            "correct": "Moist, stable air being moved over gradually rising ground by a wind."
        },
        {
            "question": "How are haze layers cleared or dispersed?",
            "choices": ["By convective mixing in cool night air.", "By wind or the movement of air.", "By evaporation similar to the clearing of fog."],
            "correct": "By wind or the movement of air."
        },
        {
            "question": "When does minimum temperature normally occur during a 24-hr period?",
            "choices": ["After sunrise.", "About 1 hour before sunrise.", "At midnight."],
            "correct": "After sunrise."
        },
        {
            "question": "Which term applies when the temperature of the air changes by compression or expansion with no heat added or removed?",
            "choices": ["Katabatic.", "Advection.", "Adiabatic."],
            "correct": "Adiabatic."
        },
        {
            "question": "Which process causes adiabatic cooling?",
            "choices": ["Expansion of air as it rises.", "Movement of air over a colder surface.", "Release of latent heat during the evaporation process."],
            "correct": "Expansion of air as it rises."
        },
        {
            "question": "What weather condition occurs at the latitude where the dewpoint lapse rate and the dry adiabatic lapse rate converge?",
            "choices": ["Cloud bases form.", "Precipitation starts.", "Stable air changes to unstable air."],
            "correct": "Cloud bases form."
        },
        {
            "question": "Which type wind flows downslope becoming warmer and dryer?",
            "choices": ["Land breeze.", "Valley wind.", "Katabatic wind."],
            "correct": "Katabatic wind."
        },
        {
            "choices": ["The air is unstable.", "A temperature inversion exists.", "The air is stable."],
            "question": "What is indicated about an air mass if the temperature remains unchanged or decreases slightly as altitude increased?",
            "correct": "The air is stable."
        },
        {
            "question": "Which condition is present when a local parcel of air is stable?",
            "choices": ["The parcel of air resists convection.", "The parcel of air cannot be forced uphill.", "As the parcel of air moves upward, its temperature becomes warmer than the surrounding air."],
            "correct": "The parcel of air resists convection."
        },
        {
            "question": "When saturated air moves downhill, its temperature increases:",
            "choices": ["At a faster rate than dry air because of the release of latent heat.", "At a slower rate than dry air because vaporization uses heat.", "At a slower rate than dry air because condensation Releases heat."],
            "correct": "At a slower rate than dry air because vaporization uses heat."
        },
        {
            "question": "What condition produces the most frequent type of ground- or surface-based temperature inversion?",
            "choices": ["The movement of colder air under warm air or the movement of warm air over the cold air.", "Widespread sinking of air within a thick layer aloft resulting in heating by compression.", "Terrestrial radiation on a clear, relatively calm night."],
            "correct": "Terrestrial radiation on a clear, relatively calm night."
        },
        {
            "question": "What characterizes a ground-based inversion?",
            "choices": ["Convection currents at the surface.", "Cold temperatures.", "Poor visibility."],
            "correct": "Poor visibility."
        },
        {
            "question": "Which is a necessary condition for the occurrence of a low-level temperature inversion wind shear?",
            "choices": ["A top wind speed differential of at least 25 knots.", "A calm or light wind near the surface and a relatively strong wind just above the inversion.", "A severe wind direction difference."],
            "correct": "A calm or light wind near the surface and a relatively strong wind just above the inversion."
        },
        {
            "question": "En route at FL 270, the altimeter is set correctly. On descent, a pilot fails to set the local altimeter setting of 30.57 hPa. If the field elevation is 650 ft, what will it indicate upon landing?",
            "choices": ["585 ft.", "1,300 ft.", "Sea level."],
            "correct": "Sea level."
        },
        {
            "question": "If the ambient temperature is colder than standard at FL 310, what is the relationship between true altitude and pressure altitude?",
            "choices": ["They are both the same, 31,000 ft.", "True altitude is lower than 31,000 ft.", "Pressure altitude is lower than true altitude."],
            "correct": "True altitude is lower than 31,000 ft."
        },
        {
            "question": "If the ambient temperature is warmer than standard at FL 350, what is the density altitude compared to pressure altitude?",
            "choices": ["Lower than pressure altitude.", "Higher than pressure altitude.", "Impossible to determine without intermediate data."],
            "correct": "Higher than pressure altitude."
        },
        {
            "question": "What is corrected altitude?",
            "choices": ["Pressure altitude corrected for instrument error.", "Indicated altitude corrected for temperature variation from standard.", "Density altitude corrected for temperature variation from standard."],
            "correct": "Indicated altitude corrected for temperature variation from standard."
        },
        {
            "question": "Which pressure is defined as station pressure?",
            "choices": ["Altimeter setting.", "Actual pressure of field elevation.", "Station barometric pressure reduced to sea level."],
            "correct": "Actual pressure of field elevation."
        },
        {
            "question": "What is the result when water vapor changes to the liquid state while being lifted in a thunderstorm?",
            "choices": ["Latent heat is released to the atmosphere.", "Latent heat is transformed into pure energy.", "Latent heat is absorbed from the surrounding air by the water droplet."],
            "correct": "Latent heat is released to the atmosphere."
        },
        {
            "question": "Convective clouds which penetrate a stratus layer can produce which threat to instrument flight?",
            "choices": ["Freezing rain.", "Clear air turbulence.", "Embedded thunderstorms."],
            "correct": "Embedded thunderstorms."
        },
        {
            "question": "What feature is normally associated with the cumulus stage of a thunderstorm?",
            "choices": ["Beginning of rain at the surface.", "Frequent lightning.", "Continuous updraft."],
            "correct": "Continuous updraft."
        },
        {
            "question": "Why are downdrafts in a mature thunderstorm hazardous?",
            "choices": ["Downdrafts are kept cool by cold rain which tends to accelerate the downward velocity.", "Downdrafts converge toward a central location under the storm after striking the surface.", "Downdrafts become warmer than the surrounding air and reverse into an updraft before reaching the surface."],
            "correct": "Downdrafts are kept cool by cold rain which tends to accelerate the downward velocity."
        },
        {
            "question": "What is a difference between an air mass thunderstorm and steady state thunderstorm?",
            "choices": ["Air mass thunderstorms produce precipitation which falls outside of the updraft.", "Air mass thunderstorm downdrafts and precipitation retard and reverse the updrafts.", "Steady-state thunderstorms are associated with local surface heating."],
            "correct": "Air mass thunderstorm downdrafts and precipitation retard and reverse the updrafts."
        },
        {
            "question": "Which type storms are most likely to produce funnel clouds or tornadoes?",
            "choices": ["Air mass thunderstorms.", "Cold front or squall line thunderstorms.", "Storms associated with icing and supercooled water."],
            "correct": "Cold front or squall line thunderstorms."
        },
        {
            "question": "Which type cloud is associated with violent turbulence and a tendency toward the production of funnel clouds?",
            "choices": ["Cumulonimbus mamma.", "Standing lenticular.", "Stratocumulus."],
            "correct": "Cumulonimbus mamma."
        },
        {
            "question": "Atmospheric pressure changes due to a thunderstorm will be at the lowest value:",
            "choices": ["During the downdraft and heavy rain showers.", "When the thunderstorm is approaching.", "Immediately after the rain showers have stopped."],
            "correct": "When the thunderstorm is approaching."
        },
        {
            "question": "A clear area in a line of thunderstorm echoes on a radar scope indicates:",
            "choices": ["The absence of clouds in the area.", "An area of no convective turbulence.", "An area where precipitation drops are not detected."],
            "correct": "An area where precipitation drops are not detected."
        },
        {
            "question": "When flying over the top of a severe thunderstorm, the cloud should be overflown by at least:",
            "choices": ["1,000 ft for each 10 knots windspeed.", "2,500 ft.", "500 ft above any moderate to severe turbulence layer."],
            "correct": "1,000 ft for each 10 knots windspeed."
        },
        {
            "question": "Freezing rain encountered during climb is normally evidence that:",
            "choices": ["A climb can be made to a higher altitude without encountering more than light icing.", "A layer of warmer air exists above.", "Ice pellets at higher altitudes have changed to rain in the warmer air below."],
            "correct": "A layer of warmer air exists above."
        },
        {
            "question": "What condition is indicated when ice pellets are encountered during flight?",
            "choices": ["Thunderstorms at higher levels.", "Freezing rain at higher levels.", "Snow at higher levels."],
            "correct": "Freezing rain at higher levels."
        },
        {
            "question": "What temperature condition is indicated if precipitation in the form of wet snow occurs during flight?",
            "choices": ["Temperature is above freezing at flight altitude.", "The temperature is above freezing at higher altitudes.", "There is an inversion with colder air below."],
            "correct": "Temperature is above freezing at flight altitude."
        },
        {
            "question": "When will frost most likely form on an aircraft?",
            "choices": ["On clear nights with stable air and light winds.", "On overcast nights with freezing drizzle precipitation.", "On clear nights with convective action and a small temperature/dewpoint spread."],
            "correct": "On clear nights with stable air and light winds."
        },
        {
            "question": "What is a feature of supercooled water?",
            "choices": ["The water drop sublimates to an ice particle upon impact.", "The unstable water drop freezes upon striking an exposed object.", "The temperature of the water drop remains at 0°C until it impacts a part of the airframe, then clear ice accumulates."],
            "correct": "The unstable water drop freezes upon striking an exposed object."
        },
        {
            "question": "Which type precipitation is an indication that supercooled water is present?",
            "choices": ["Wet snow.", "Freezing rain.", "Ice pellets."],
            "correct": "Freezing rain."
        },
        {
            "question": "What condition is necessary for the formation of structural icing in flight?",
            "choices": ["Supercooled water drops.", "Water vapor.", "Visible water."],
            "correct": "Visible water."
        },
        {
            "question": "Which type of icing is associated with the smallest size of water droplet similar to that found in low-level stratus clouds?",
            "choices": ["Clear ice.", "Frost ice.", "Rime ice."],
            "correct": "Rime ice."
        },
        {
            "question": "What is a characteristic of the troposphere?",
            "choices": ["It contains all moisture of the atmosphere.", "There is an overall decrease of temperature with an increase of altitude.", "The average altitude of the top of the troposphere is about 6 miles."],
            "correct": "There is an overall decrease of temperature with an increase of altitude."
        },
        {
            "question": "What weather feature occurs at altitude levels near the tropopause?",
            "choices": ["Maximum winds and narrow wind shear zones.", "Abrupt temperature increase above the tropopause.", "Thin layers of cirrus (ice crystal) clouds at the tropopause level."],
            "correct": "Maximum winds and narrow wind shear zones."
        },
        {
            "question": "Where do the maximum winds associated with the jetstream usually occur?",
            "choices": ["In the vicinity of breaks in the tropopause on the polar side of the jet core.", "Below the jet core where a long straight stretch of the jetstream is located.", "On the equatorial side of the jetstream where moisture has formed cirriform clouds."],
            "correct": "In the vicinity of breaks in the tropopause on the polar side of the jet core."
        },
        {
            "question": "Where are jetstreams normally located?",
            "choices": ["in areas of strong low pressure systems in the stratosphere.", "In a break in the tropopause where intensified temperature gradients are located.", "In a single continuous band, encircling the earth, where there is a break between the equatorial and polar tropopause."],
            "correct": "In a break in the tropopause where intensified temperature gradients are located."
        },
        {
            "question": "Where is the normal location of the jetstream relative to surface lows and fronts?",
            "choices": ["The jetstream is located north of the surface systems.", "The jetstream is located south of the low and warm front.", "The jetstream is located over the low and crosses both the warm front and the cold front."],
            "correct": "The jetstream is located north of the surface systems."
        },
        {
            "question": "Which type frontal system is normally crossed by the jetstream?",
            "choices": ["Cold front and warm front.", "Warm front", "Occluded front."],
            "correct": "Occluded front."
        },
        {
            "question": "Which type clouds may be associated with the jetstream?",
            "choices": ["Cumulonimbus cloud line where the jetstream crosses the cold front.", "Cirrus clouds on the equatorial side of the jetstream.", "Cirrostratus cloud band on the polar side and under the jetstream."],
            "correct": "Cirrus clouds on the equatorial side of the jetstream."
        },
        {
            "question": "A strong wind shear can be expected:",
            "choices": ["On the low pressure side of a 100 knots jetstream core.", "Where the horizontal wind shear is 15 knots, in a distance equal to 2.5° longitude.", "If the 5°C isotherms are spaced 100 NM or closer together."],
            "correct": "On the low pressure side of a 100 knots jetstream core."
        },
        {
            "question": "Which area or areas of the Northern Hemisphere experience a generally east to west movement of weather systems?",
            "choices": ["Arctic only.", "Arctic and subtropical.", "Subtropical only."],
            "correct": "Arctic and subtropical."
        },
        {
            "question": "Summer thunderstorms in the arctic region will generally move:",
            "choices": ["Northeast to southwest in polar easterlies.", "Southwest to northeast with the jetstream flow.", "Directly north to south with the low-level polar airflow."],
            "correct": "Northeast to southwest in polar easterlies."
        },
        {
            "question": "Which arctic flying hazard is caused when a cloud layer of uniform thickness overlies a snow or ice covered surface?",
            "choices": ["Ice fog.", "Whiteout.", "Blowing snow."],
            "correct": "Whiteout."
        },
        {
            "question": "Which weather condition is present when the tropical storm is upgraded to hurricane?",
            "choices": ["Highest windspeed, 100knots or more.", "A clear area or hurricane eye has formed.", "Sustained winds of 65 knots or more."],
            "correct": "Sustained winds of 65 knots or more."
        },
        {
            "question": "A squall is a sudden increase of at least 16 knots in average wind speed to a sustained speed of:",
            "choices": ["24 knots or more for at least 1 minute.", "20 knots or more for at least 1 minute.", "22 knots or more for at least 1 minute."],
            "correct": "22 knots or more for at least 1 minute."
        },
        {
            "question": "Which are the only cloud types forecast in the terminal aerodrome forecast?",
            "choices": ["Altocumulus.", "Cumulonimbus.", "Stratocumulus."],
            "correct": "Cumulonimbus."
        },
        {
            "question": "What is the single source reference that contains information regarding volcanic eruption, turbulence, and icing conditions for a specific region?",
            "choices": ["Weather depiction chart.", "In-flight weather advisories.", "Area forecast."],
            "correct": "In-flight weather advisories."
        },
        {
            "question": "A severe thunderstorm is one in which the surface wind is:",
            "choices": ["58 mph or greater and/or surface hail is 3/4 inch or more in diameter.", "50 knots or greater and/or surface hail is 1/2 inch or more in diameter.", "40 knots or greater and/or surface hail is 1 inch or more in diameter."],
            "correct": "58 mph or greater and/or surface hail is 3/4 inch or more in diameter."
        },
        {
            "question": "What is the period covered by the outlook section of the convective SIGMET?",
            "choices": ["24 hours after the valid time.", "2-6 hours after the valid time.", "No more than 2 hours after the valid time."],
            "correct": "No more than 2 hours after the valid time."
        },
        {
            "question": "Which is a definition of a 'severe wind shear'?",
            "choices": [
                "Any rapid change of horizontal wind shear in excess of 25 knots, vertical shear excepted.",
                "Any rapid change in wind direction or velocity which causes airspeed changes greater than 15 knots or vertical speed changes greater than 500 fpm.",
                "Any change of airspeed greater than 20 knots which is sustained for more than 20 seconds or vertical speed changes in excess of 100fpm."
            ],
            "correct": "Any rapid change in wind direction or velocity which causes airspeed changes greater than 15 knots or vertical speed changes greater than 500 fpm."
        },
        {
            "question": "Clear air turbulence associated with a mountain wave may extend as far as:",
            "choices": ["1,000 miles or more downstream of the mountain.", "5,000 ft above the tropopause.", "100 miles or more upwind of the mountain."],
            "correct": "5,000 ft above the tropopause."
        },
        {
            "question": "Which type jetstream can be expected to cause the greater turbulence?",
            "choices": ["A straight jetstream with high horizontal core shear.", "A curving jetstream associated with a deep low pressure trough.", "A jetstream flowing over an active high-pressure ridge."],
            "correct": "A curving jetstream associated with a deep low pressure trough."
        },
        {
            "question": "What happens to residual ice that remains after deice boots are inflated and shed ice?",
            "choices": ["Residual ice increases with a decrease in airspeed or temperature.", "Residual ice remains the same until the aircraft exits icing conditions.", "Residual ice decreases with a decrease in airspeed or temperature."],
            "correct": "Residual ice remains the same until the aircraft exits icing conditions."
        },
        {
            "question": "The most susceptible surface of aircraft for ice accumulation is the:",
            "choices": ["Windshield.", "Main wing.", "Tailplane."],
            "correct": "Tailplane."
        },
        {
            "question": "If you detect icing accumulation in flight, especially if the aircraft is not equipped with a deicing system, you should:",
            "choices": ["Move to a higher altitude.", "Leave the area of precipitation, if able or fly to an altitude where the temperature is above freezing.", "Fly to an area with liquid precipitation."],
            "correct": "Leave the area of precipitation, if able or fly to an altitude where the temperature is above freezing."
        },
        {
            "question": "When conditions favoring the formation of ice are present, pilots should check for ice accumulation prior to flight. The best way to do this is by:",
            "choices": ["Using a flashlight and watching for light reflection.", "Running your hand along all control surfaces.", "Using ice detection lights."],
            "correct": "Running your hand along all control surfaces."
        },
        {
            "question": "To recover from a tailplane stall brought on by ice accumulation, the pilot should:",
            "choices": ["Retract flaps and increase power, but only to compensate for the reduction in lift.", "Decrease power and maintain a speed below VA.", "Extend the flaps and reduce power to slow the aircraft."],
            "correct": "Retract flaps and increase power, but only to compensate for the reduction in lift."
        },
        {
            "question": "Tailplane icing can be detected by a(n):",
            "choices": ["Increase in elevator effectiveness.", "Gradual uncommanded nose-up pitch.", "Sudden uncommanded nose-down pitch."],
            "correct": "Sudden uncommanded nose-down pitch."
        },
        {
            "question": "Tailplane icing can also be detected by:",
            "choices": ["Elevator control pulsing, oscillations or vibrations.", "A gradual uncommanded reduction in engine power.", "An increase in elevator effectiveness."],
            "correct": "Elevator control pulsing, oscillations or vibrations."
        },
        {
            "question": "In an aircraft equipped with a pneumatic deicing system, the appropriate technique for removing ice is to:",
            "choices": ["Operate the pneumatic deicing system several times.", "Operate pneumatic deicing system once.", "Confirm that ice has accumulated prior to engaging the pneumatic boots."],
            "correct": "Confirm that ice has accumulated prior to engaging the pneumatic boots."
        },
        {
            "question": "A tailplane stall as the result of ice accumulation is most likely to occur during:",
            "choices": ["Cruise flight.", "Approach and landing.", "An instrument holding pattern."],
            "correct": "Approach and landing."
        },
        {
            "question": "What determines how icing is reported on a PIREP?",
            "choices": ["Type of ice.", "Thickness of ice.", "Rate of accumulation."],
            "correct": "Rate of accumulation."
        },
        {
            "question": "Clouds are classified into four structural families, according to their:",
            "choices": ["Genera, species, varieties, supplemental features & accessory clouds, mother-clouds.", "Density, composition, water vapor concentration, and relative thickness.", "Height, including high, middle, low, and those with extensive vertical development."],
            "correct": "Height, including high, middle, low, and those with extensive vertical development."
        },
        {
            "question": "Variations in altimeter settings across different geographical areas are primarily affected by:",
            "choices": ["The specific humidity profiles of the low atmosphere.", "The horizontal and vertical distribution of temperature.", "Localized Coriolis variations over coastal sectors."],
            "correct": "The horizontal and vertical distribution of temperature."
        },

        # --- Flashcard Section ---
        {
            "question": "To which meteorological condition does the term 'dewpoint' refer?",
            "choices": [],
            "correct": "The temperature to which air must be cooled to become saturated."
        },
        {
            "question": "What temperature condition is indicated if wet snow is encountered at your flight altitude?",
            "choices": [],
            "correct": "The temperature is above freezing at your altitude."
        },
        {
            "question": "The amount of water vapor which air can hold largely depends on what factor?",
            "choices": [],
            "correct": "Air temperature."
        },
        {
            "question": "Clouds, fog, or dew will always form when what occurs?",
            "choices": [],
            "correct": "Water vapor condenses."
        },
        {
            "question": "What causes surface winds to flow across the isobars at an angle rather than parallel to them?",
            "choices": [],
            "correct": "Surface friction."
        },
        {
            "question": "Winds at 5,000 feet AGL on a particular flight are southwesterly while most of the surface winds are southerly. This difference in direction is primarily due to:",
            "choices": [],
            "correct": "friction between the wind and the surface."
        },
        {
            "question": "What relationship exists between the winds at 2,000 feet above the surface and the surface winds?",
            "choices": [],
            "correct": "The winds at 2,000 feet tend to parallel the isobars while the surface winds cross the isobars at an angle toward lower pressure and are weaker."
        },
        {
            "question": "Which force, in the Northern Hemisphere, acts at a right angle to the wind and deflects it to the right until parallel to the isobars?",
            "choices": [],
            "correct": "Coriolis force."
        },
        {
            "question": "Altimeter setting is the value to which the scale of the pressure altimeter is set so the altimeter indicates what at field elevation?",
            "choices": [],
            "correct": "True altitude at field elevation."
        },
        {
            "question": "The most frequent type of ground or surface based temperature inversion is that produced by what physical mechanism?",
            "choices": [],
            "correct": "Terrestrial radiation on a clear, relatively calm night."
        },
    ],
    "Human Performance": [
        # --- Multiple Choice Section ---
        {
            "question": "What is the time of useful consciousness at 20,000 feet (moderate activity)?",
            "choices": ["5 minutes", "1 minute", "10 minutes", "30 seconds"],
            "correct": "5 minutes"
        },
        {
            "question": "What is the absolute time a pilot should stop drinking before flying?",
            "choices": [
                "6 hours but it depends upon the amount of alcohol that has been consumed",
                "24 hours but it depends upon the amount of alcohol that has been consumed",
                "12 hours but it depends upon the amount of alcohol that has been consumed",
                "8 hours but it depends upon the amount of alcohol that has been consumed"
            ],
            "correct": "8 hours but it depends upon the amount of alcohol that has been consumed"
        },
        {
            "question": "With regards to procedures, a pilot is advised to:",
            "choices": [
                "Memorize all procedures as carefully as possible",
                "Memorize immediate actions and subsequent actions",
                "Memorize immediate actions and refer to check list for subsequent actions",
                "Rely on the checklist for all procedures"
            ],
            "correct": "Memorize immediate actions and refer to check list for subsequent actions"
        },
        {
            "question": "What should a Captain do before making a non-urgent decision?",
            "choices": [
                "Put his own view forward and then ask for the opinions of other members of the crew",
                "Consider all implications",
                "Encourage ideas from the crew before stating his own opinion",
                "Monitor his motor programme (flying)"
            ],
            "correct": "Encourage ideas from the crew before stating his own opinion"
        },
        {
            "question": "Discussing private matters in the cockpit:",
            "choices": [
                "Decreases the captain's role in leadership",
                "Should be avoided in flight",
                "Can improve team spirit",
                "Is appropriate at any stage of the flight"
            ],
            "correct": "Can improve team spirit"
        },
        {
            "question": "The co-pilot is responsible for monitoring the implementation of the Commander's decision.",
            "choices": ["True", "False"],
            "correct": "False"
        },
        {
            "question": "During a general briefing at the pre-flight stage, the captain should emphasize:",
            "choices": [
                "The complete delegation of all duties",
                "The importance of crew coordination",
                "The priority of departing on schedule",
                "The avoidance of inadequate handling of controls"
            ],
            "correct": "The importance of crew coordination"
        },
        {
            "question": "Decision making in emergency situations requires primarily:",
            "choices": [
                "Speed of reaction",
                "The distribution of tasks and crew coordination",
                "Strong situational awareness",
                "The whole crew to focus on the immediate problem"
            ],
            "correct": "The distribution of tasks and crew coordination"
        },
        {
            "question": "The effects of carbon monoxide:",
            "choices": [
                "Increases with altitude",
                "Decreases with altitude",
                "Increases with increase of density",
                "Decreases with pressure loss"
            ],
            "correct": "Increases with altitude"
        },
        {
            "question": "A pilot suffering from hyperventilation during final approach in poor weather can combat the effects by:",
            "choices": [
                "Go on 100% oxygen and go around",
                "Land regardless of the weather",
                "Regulate depth and rate of breathing",
                "Declare a mayday"
            ],
            "correct": "Regulate depth and rate of breathing"
        },
        {
            "question": "The best strategies to increase stress tolerance are:",
            "choices": [
                "Planning, experience and self-control (fewer unexpected situation)",
                "Learning, experience and anticipation",
                "Learning, experience and CRM",
                "Planning, experience and CRM"
            ],
            "correct": "Learning, experience and CRM"
        },
        {
            "question": "Disorientation is more likely when the pilot is:\n1. flying in IMC\n2. frequently changing between inside and outside references\n3. flying from IMC to VMC\n4. approaching over still water at night",
            "choices": [
                "1, 2 & 3 only are correct",
                "1, 2 & 4 only are correct",
                "1, 2, 3 & 4 are correct",
                "1 only is correct"
            ],
            "correct": "1, 2 & 4 only are correct"
        },
        {
            "question": "The scanning technique should differ by day and night.",
            "choices": ["True", "False"],
            "correct": "True"
        },
        {
            "question": "A pilot suffering from decompression sickness should:",
            "choices": [
                "Descend to a lower level where the symptoms will disappear and continue the flight at this or a lower level",
                "Decrease the cabin pressure to relieve the symptoms",
                "Continue the flight at a lower altitude and carry out exercises to relieve the pain in the affected site",
                "Land as soon as possible and seek medical assistance"
            ],
            "correct": "Land as soon as possible and seek medical assistance"
        },
        {
            "question": "A pilot who is diagnosed as having an alcohol problem can:",
            "choices": [
                "Continue to fly as an operating pilot whilst he receives treatment",
                "Never fly again as an operating pilot",
                "Fly as a pilot only if he is supervised by another pilot",
                "Return to flying duties as a suitable course of treatment is complete"
            ],
            "correct": "Return to flying duties as a suitable course of treatment is complete"
        },
        {
            "question": "The Critical Zone of hypoxia begins at:",
            "choices": ["18,000ft", "20,000ft", "23,000ft", "3,600ft"],
            "correct": "20,000 ft"
        },
        {
            "question": "What should the pilot rely on if disoriented in IMC?",
            "choices": ["Vision", "Turning head to recover from disorientation", "Sense of balance", "Instruments"],
            "correct": "Instruments"
        },
        {
            "question": "What four factors affect night vision?",
            "choices": [
                "Age, alcohol, altitude and smoking",
                "Age, altitude, instrument lights and smoking",
                "Instrument lights, altitude, alcohol and smoking",
                "Age, alcohol, altitude and instrument lights"
            ],
            "correct": "Age, alcohol, altitude and smoking"
        },
        {
            "question": "If, having tried all normal methods, the ears cannot be cleared in flight, the following action should be taken:",
            "choices": [
                "Ignore and it will go away",
                "Descend to 10,000ft or MSA - whichever is higher",
                "Seek medical advice as soon as possible",
                "Descend as quickly as possible to minimize pain"
            ],
            "correct": "Seek medical advice as soon as possible"
        },
        {
            "question": "How will an oncoming aircraft on a line of constant bearing appear visually?",
            "choices": [
                "There will be no relative movement and it will appear to be very small until seconds before the collision",
                "There will be no relative movement and it will appear to be very small until seconds before the aircraft passes close by",
                "There will be no relative movement and it will appear to be very small until seconds before the aircraft passes above",
                "There will be no relative movement and it will appear to be very small until seconds before the aircraft passes well clear"
            ],
            "correct": "There will be no relative movement and it will appear to be very small until seconds before the collision"
        },
        {
            "question": "What visual technique should be used when searching for an aircraft?",
            "choices": [
                "Sweep from side to side with the eyes covering the whole field of vision",
                "Search the sky portion by portion starting on the left",
                "Pinpoint 10° segments of the sky and confirm before passing onto another",
                "Use a succession of small and rapid eye movements"
            ],
            "correct": "Pinpoint 10° segments of the sky and confirm before passing onto another"
        },
        {
            "question": "What are the personality traits of a good pilot?",
            "choices": ["Reliable and stable", "Stable and extraverted", "Reliable and extraverted", "Reliable, calm and extraverted"],
            "correct": "Reliable and stable"
        },
        {
            "question": "What are the key points of a good briefing?",
            "choices": [
                "Individual, understood and simple",
                "Individual, clear and simple",
                "Individual, understood and short",
                "Simple, clear, understood and individual"
            ],
            "correct": "Individual, understood and short"
        },
        {
            "question": "The most obvious sign of an individual suffering from carbon monoxide poisoning is:",
            "choices": [
                "Muscular impairment",
                "Cyanosis of the lips and fingernails",
                "Sensory loss, particularly tunnelling of vision",
                "Cherry red lips and flushed cheeks"
            ],
            "correct": "Cherry red lips and flushed cheeks"
        },
        {
            "question": "A sensation of tumbling and dizziness when a pilot makes movement of his/her head during a tight turn are symptoms of:",
            "choices": ["The Occulogyral Effect", "Flicker-vertigo", "Pilot's Vertigo", "Nystagmus"],
            "correct": "Pilot's Vertigo"
        },
        {
            "question": "If you switch on the anti-collision light in IMC, what are the likely effects?",
            "choices": [
                "Depth perception increases",
                "You can suffer from dizziness and disorientation",
                "You can suffer from Color Illusion",
                "Binocular vision is affected"
            ],
            "correct": "You can suffer from dizziness and disorientation"
        },
        {
            "question": "The illusion that the aircraft is taxiing too fast can be caused by:",
            "choices": ["Snow and a tailwind", "Snow and a headwind", "Rain and a headwind", "An unaccustomed high distance of the cockpit from the ground"],
            "correct": "An unaccustomed high distance of the cockpit from the ground"
        },
        {
            "question": "A pilot can improve the probability of detecting other aircrafts by:",
            "choices": [
                "Minimizing the duration of eye rests and making as many eye movements as possible",
                "Moving the head frequently to alter the apparent motion of any distant object",
                "Maximizing the time spent looking in each sector to allow the maximum chance of detecting movement",
                "Maintaining as far as possible a lookout ahead of the aircraft and relying on peripheral vision to detect any movement from the side"
            ],
            "correct": "Minimizing the duration of eye rests and making as many eye movements as possible"
        },
        {
            "question": "How do misty/foggy conditions affect the pilot's judgment on the approach?",
            "choices": [
                "Underestimating range due to illusionary effect through the cockpit glass",
                "Underestimating range due to the lights appearing dim",
                "Overestimating range due to illusionary effect through the cockpit glass",
                "Overestimating range due to the lights appearing dim"
            ],
            "correct": "Overestimating range due to the lights appearing dim"
        },
        {
            "question": "Communication in the cockpit is primarily used for what purpose?",
            "choices": [
                "It is the main tool to ensure coordination",
                "It is the main tool to ensure comprehension",
                "It is the main tool to ensure harmony",
                "It is the main tool to ensure understanding"
            ],
            "correct": "It is the main tool to ensure coordination"
        },

        # --- Flashcard Section ---
        {
            "question": "Decompression sickness is caused by what physical phenomenon?",
            "choices": [],
            "correct": "nitrogen bubbles coming out of solution in the blood to form bubbles in the body tissues"
        },
        {
            "question": "List the classic clinical signs and symptoms of carbon monoxide poisoning.",
            "choices": [],
            "correct": "Ruddy complexion, headache, tightness across the forehead, impaired judgement"
        },
        {
            "question": "Will smokers experience hypoxia at a lower or higher cabin altitude than non-smokers?",
            "choices": [],
            "correct": "at a lower cabin altitude"
        },
        {
            "question": "Immediate treatment of carbon monoxide poisoning on the ground should include what action?",
            "choices": [],
            "correct": "stop all smoking"
        },
        {
            "question": "What is one of the distinct initial neurological indications of Hypoxia?",
            "choices": [],
            "correct": "Impaired judgement"
        },
        {
            "question": "What are the core timeline restrictions to flying after performing scuba diving?",
            "choices": [],
            "correct": "No flying within 24 hours if a depth of 30 feet has been exceeded, otherwise the limit is 12 hours"
        },
        {
            "question": "Are there any specific flight restrictions to a pilot who has been snorkelling and has exceeded a depth of 30 feet?",
            "choices": [],
            "correct": "No"
        },
        {
            "question": "Hypoxic Hypoxia directly impairs night vision capability. (True / False)",
            "choices": [],
            "correct": "True"
        },
        {
            "question": "What is the very first action that must be taken by the pilot in the event of an explosive or rapid cabin decompression above 10,000 feet?",
            "choices": [],
            "correct": "Don oxygen mask and check oxygen flow"
        },
        {
            "question": "If the symptoms of hyperventilation occur at an operational altitude where hypoxia is not a consideration, what is the correct remedial action?",
            "choices": [],
            "correct": "Decrease rate and depth of breathing"
        },
        {
            "question": "What hobby/activity significantly increases the risk of Decompression Sickness (DCS) occurring in flight?",
            "choices": [],
            "correct": "scuba diving shortly before flight"
        },
        {
            "question": "In typical commercial transport aircraft, cabin pressure is normally regulated and maintained at what altitude range?",
            "choices": [],
            "correct": "6,000 - 8000 ft"
        },
        {
            "question": "In the event of a passenger or crew member showing clear symptoms of DCS, what must the aircraft do?",
            "choices": [],
            "correct": "land as soon as possible"
        },
        {
            "question": "Breathing 100% oxygen at an altitude of 40,000 ft is physiologically equivalent to breathing normally at what ambient altitude?",
            "choices": [],
            "correct": "10,000 ft"
        },
        {
            "question": "A prudent pilot should avoid flying for a baseline of at least how many hours after consuming small amounts of alcohol?",
            "choices": [],
            "correct": "24 hours"
        },
        {
            "question": "A progressive tendency to ask leading questions during crew interactions is an early symptomatic indicator of what?",
            "choices": [],
            "correct": "decreased situational awareness"
        },
        {
            "question": "Refraction, caused directly by rain on the windscreen, impacts the visual glide path by making the approach appear:",
            "choices": [],
            "correct": "shaller / shallower"
        },
        {
            "question": "The visual blooming effect caused by heavy rain brings about what specific illusion regarding the runway?",
            "choices": [],
            "correct": "the runway appear closer"
        },
        {
            "question": "A standard and disciplined visual scan should divide and cover the sky in overlapping segments of how many degrees?",
            "choices": [],
            "correct": "10 deg"
        },
        {
            "question": "A distant aircraft is identified and remains on a perfectly constant relative bearing. What action should you take?",
            "choices": [],
            "correct": "Take immediate avoiding action"
        },
        {
            "question": "When turning in IMC, head movements should be strictly kept to a minimum to prevent the activation of which sensory illusion?",
            "choices": [],
            "correct": "Coriolis effect"
        },
        {
            "question": "Even with a small ingestion of alcohol, how is a pilot's baseline physiology altered regarding altitude changes?",
            "choices": [],
            "correct": "the pilot will be more susceptible to hypoxia"
        },
        {
            "question": "If suffering from Hypoxia, what are the three immediate corrective actions required?",
            "choices": [],
            "correct": "descend to below 10,000 ft, go onto 100% oxygen, and reduce activity"
        }
    ],
   "Communications": [
        # --- Multiple Choice Section ---
        {
            "question": "The term 'RECLEARED' means that:",
            "choices": [
                "A change has been made to your last clearance and this new clearance supersedes your previous clearance",
                "You are authorized to proceed via the same route as your previous leg",
                "Your departure routing has been cancelled",
                "The current clearance limit is removed"
            ],
            "correct": "A change has been made to your last clearance and this new clearance supersedes your previous clearance"
        },
        {
            "question": "The phrase used to separate portions of a message is:",
            "choices": ["Break", "Correction", "Separation", "Roger"],
            "correct": "Break"
        },
        {
            "question": "An example of a general call is:",
            "choices": ["All stations", "Any station info", "Broadcast standard", "CQ CQ"],
            "correct": "All stations"
        },
        {
            "question": "The condition that describes the state of an aircraft in serious and/or imminent danger and requiring immediate assistance is:",
            "choices": ["Distress", "Urgency", "Emergency", "Alerting"],
            "correct": "Distress"
        },
        {
            "question": "Your reply to the message 'REPORT FLIGHT CONDITONS' should be:",
            "choices": ["VMC/IMC", "Visual / Instrumental", "Maintaining flight plan", "Clear or Clouded"],
            "correct": "VMC/IMC"
        },
        {
            "question": "The phrase 'BRAKING CO-EFFICIENT 20' from ATC means that the braking action is:",
            "choices": ["Good", "Medium to Good", "Medium", "Poor"],
            "correct": "Poor"
        },
        {
            "question": "An altitude of 13,500 feet would be spoken as:",
            "choices": [
                "One three thousand five hundred feet",
                "Thirteen thousand five hundred feet",
                "One three thousand five hundred",
                "Thirteen point five thousand feet"
            ],
            "correct": "One three thousand five hundred feet"
        },
        {
            "question": "How does ATC report RVR?",
            "choices": [
                "In meters at touchdown, mid-point and stop-end of runway",
                "In feet along the entire length of the active track",
                "In visibility codes matching the GAFOR matrix",
                "Only at the touchdown sector unless requested otherwise"
            ],
            "correct": "In meters at touchdown, mid-point and stop-end of runway"
        },
        {
            "question": "Readability 2 means that your transmission is:",
            "choices": ["Readable with difficulty", "Readable now and then", "Unreadable", "Perfectly readable"],
            "correct": "Readable now and then"
        },
        {
            "question": "An urgency message should include the following information:",
            "choices": [
                "Name of station addressed, aircraft callsign, nature of urgency condition, intention of commander, position, level, heading",
                "Aircraft callsign, position, souls on board, endurance remaining",
                "Name of station, aircraft type, captain name, destination, airspeed, altitude",
                "Callsign, frequency, registration number, route code"
            ],
            "correct": "Name of station addressed, aircraft callsign, nature of urgency condition, intention of commander, position, level, heading"
        },
        {
            "question": "Following a communication failure, the time at which the aircraft should aim to leave the hold is:",
            "choices": ["EAT or ETA", "Within 3 minutes of holding pattern initialization", "At the discretion of the commander", "Upon reaching the highest assigned flight level"],
            "correct": "EAT or ETA"
        },
        {
            "question": "If a transponder is unserviceable before an IFR departure, then the pilot:",
            "choices": [
                "May proceed with the flight with ATC permission",
                "Must delay the flight until repairs are completed",
                "Can operate normally below Class A airspace only",
                "Must cancel the IFR flight plan and file under VFR"
            ],
            "correct": "May proceed with the flight with ATC permission"
        },
        {
            "question": "The response to a general call from ATC is for the aircraft to:",
            "choices": ["Give no response", "Acknowledge in order of seniority", "Acknowledge in alphabetical order of callsigns", "Respond immediately with their callsign"],
            "correct": "Give no response"
        },
        {
            "question": "The term 'CORRECTION' is used when:",
            "choices": [
                "An error has been made in the transmission and the correct version is given",
                "The message has been completely cancelled",
                "The station needs to verify the readout configuration",
                "The readback was perfectly matched"
            ],
            "correct": "An error has been made in the transmission and the correct version is given"
        },
        {
            "question": "The instruction from ATC to an aircraft to abandon its take off includes the phrase:",
            "choices": ["STOP IMMEDIATELY", "ABORT TAKEOFF", "CANCEL DEPARTURE", "HOLD IN POSITION"],
            "correct": "STOP IMMEDIATELY"
        },
        {
            "question": "The correct readback of the frequency 123.725 on 25khz spacing is:",
            "choices": ["123.725", "123.72", "123.7", "One two three point seven two five"],
            "correct": "123.725"
        },
        {
            "question": "The message 'READABILITY 3' means:",
            "choices": ["Readable but with difficulty", "Readable now and then", "Perfectly readable", "Readable with interference"],
            "correct": "Readable but with difficulty"
        },
        {
            "question": "The full range of VHF frequencies used for aeronautical communication is:",
            "choices": ["118.0 to 136.975 MHz", "108.0 to 117.95 MHz", "108.0 to 136.975 MHz", "118.0 to 151.0 MHz"],
            "correct": "118.0 to 136.975 MHz"
        },
        {
            "question": "The instruction 'ORBIT' from ATC means that the aircraft should:",
            "choices": [
                "Carry out one 360 degree turn only",
                "Hold in a non-standard oval pattern",
                "Maintain a continuous circling maneuver until advised",
                "Perform a standard 180 degree course reversal"
            ],
            "correct": "Carry out one 360 degree turn only"
        },
        {
            "question": "The best signals for VHF communications are obtained when the position of the aircraft is at:",
            "choices": [
                "High altitude and in the vicinity of the aerodrome",
                "Low altitude directly over the transmission antenna",
                "High altitude far beyond the terminal line-of-sight limits",
                "Any altitude provided a strong mountain wave reflection exists"
            ],
            "correct": "High altitude and in the vicinity of the aerodrome"
        },
        {
            "question": "Your action in response to the instruction from ATC to 'RESET SQUAWK' is to:",
            "choices": [
                "Reselect the numbers on the control unit",
                "Turn the transponder off and back to standby mode",
                "Cycle the Mode C altimeter toggle switch",
                "Squawk Ident immediately"
            ],
            "correct": "Reselect the numbers on the control unit"
        },
        {
            "question": "What is the significance of an ATC clearance which reads '... CRUISE SIX THOUSAND ...'?",
            "choices": [
                "The pilot must maintain 6,000 feet until reaching the IAF serving the destination airport, then execute the published approach procedure.",
                "Climbs may be made to, or descents made from, 6,000 feet at the pilot's discretion.",
                "The pilot may utilize any altitude from the MEA/MOCA to 6,000 feet, but each change in altitude must be reported to ATC."
            ],
            "correct": "Climbs may be made to, or descents made from, 6,000 feet at the pilot's discretion."
        },
        {
            "question": "What is the recommended climb procedure when a nonradar departure control instructs a pilot to climb to the assigned altitude?",
            "choices": [
                "Maintain an optimum climb on the centerline of the airway without intermediate level offs until 1,000 feet below assigned altitude, then 500 to 1500 feet per minute.",
                "Climb at a maximum angle of climb to within 1,000 feet of the assigned altitude, then 500 feet per minute the last 1,000 feet.",
                "Maintain a continuous optimum climb until reaching assigned altitude and report passing each 1,000 foot level."
            ],
            "correct": "Maintain an optimum climb on the centerline of the airway without intermediate level offs until 1,000 feet below assigned altitude, then 500 to 1500 feet per minute."
        },
        {
            "question": "When departing from an airport not served by a control tower, the issuance of a clearance containing a void time indicates that:",
            "choices": [
                "ATC will protect the airspace only to the void time.",
                "ATC will assume the pilot has not departed if no transmission is received before the void time.",
                "The pilot must advise ATC as soon as possible, but no later than 30 minutes, of their intentions if not off by the void time."
            ],
            "correct": "the pilot must advise ATC as soon as possible, but no later than 30 minutes, of their intentions if not off by the void time."
        },
        {
            "question": "What response is expected when ATC issues an IFR clearance to pilots of airborne aircraft?",
            "choices": [
                "Read back those parts containing altitude assignments or vectors and any part requiring verification.",
                "Read back should be unsolicited and spontaneous to confirm that the pilot understands all instructions.",
                "Read back the entire clearance as required by regulation."
            ],
            "correct": "Read back those parts containing altitude assignments or vectors and any part requiring verification."
        },
        {
            "question": "On the runup pad, you receive an abbreviated clearance 'CLEARED TO THE DALLAS LOVE AIRPORT AS FILED...'. This layout will always contain the:",
            "choices": [
                "Requested enroute altitude.",
                "Departure control frequency.",
                "Destination airport and route."
            ],
            "correct": "destination airport and route."
        },
        {
            "question": "When may ATC request a detailed report of an emergency even though a rule has not been violated?",
            "choices": [
                "When the emergency occurs in controlled airspace.",
                "Any time an emergency occurs.",
                "When priority has been given."
            ],
            "correct": "When priority has been given."
        },
        {
            "question": "Which information is always given in an abbreviated clearance?",
            "choices": [
                "Altitude to maintain and code to squawk.",
                "SID or transition name and altitude to maintain.",
                "Name of destination airport or specific fix and altitude."
            ],
            "correct": "Name of destination airport or specific fix and altitude."
        },
        {
            "question": "If a control tower and an FSS are located on the same airport, which function is provided by the FSS during those periods when the tower is closed?",
            "choices": [
                "Automatic closing of the IFR flight plan.",
                "Approach control services.",
                "Airport Advisory Service."
            ],
            "correct": "Airport Advisory Service."
        },
        {
            "question": "Which service is provided for IFR arrivals by a FSS located on an airport without a control tower?",
            "choices": [
                "Airport advisories.",
                "All functions of approach control.",
                "Automatic closing of the IFR flight plan."
            ],
            "correct": "Airport advisories."
        },
        {
            "question": "What action is recommended if a pilot does not wish to use an instrument departure procedure?",
            "choices": [
                "Advise clearance delivery or ground control before departure.",
                "Advise departure control upon initial contact.",
                "Enter 'No DP' in the REMARKS section of the IFR flight plan."
            ],
            "correct": "Enter 'No DP' in the REMARKS section of the IFR flight plan."
        },
        {
            "question": "During a takeoff into IFR conditions with low ceilings, when should the pilot contact departure control?",
            "choices": [
                "Upon completing the first turn after takeoff or upon establishing cruise climb on a straight out departure.",
                "When advised by the tower.",
                "Before penetrating the clouds."
            ],
            "correct": "When advised by the tower."
        },
        {
            "question": "During a flight, the controller advises 'traffic 2 o'clock 5 miles southbound.' The pilot is holding 20° correction for a crosswind from the right. Where should the pilot look for the traffic?",
            "choices": [
                "40° to the right of the airplane's nose.",
                "20° to the right of the airplane's nose.",
                "Straight ahead."
            ],
            "correct": "40° to the right of the airplane's nose."
        },
        {
            "question": "What is meant when departure control instructs you to 'resume own navigation' after you have been vectored to a Victor airway?",
            "choices": [
                "You should maintain the airway by use of your navigation equipment.",
                "You are still in radar contact, but must make position reports.",
                "Radar service is terminated."
            ],
            "correct": "You should maintain the airway by use of your navigation equipment."
        },
        {
            "question": "What does the ATC term 'Radar Contact' signify?",
            "choices": [
                "Your aircraft has been identified and you will receive separation from all aircraft while in contact with this radar facility.",
                "Your aircraft has been identified on the radar display and radar flight following will be provided until radar identification is terminated.",
                "You will be given traffic advisories until advised the service has been terminated or that radar contact has been lost."
            ],
            "correct": "Your aircraft has been identified on the radar display and radar flight following will be provided until radar identification is terminated."
        },
        {
            "question": "Upon intercepting the assigned radial, the controller advises you that you are on the airway and to 'RESUME OWN NAVIGATION.' This phrase means that:",
            "choices": [
                "You are still in radar contact, but must make position reports.",
                "You are to assume responsibility for your own navigation.",
                "Radar services are terminated and you will be responsible for position reports."
            ],
            "correct": "you are to assume responsibility for your own navigation."
        },
        {
            "question": "Which clearance procedures may be issued by ATC without prior pilot request?",
            "choices": [
                "DP's, STAR's, and contact approaches.",
                "Contact and visual approaches.",
                "DP's, STAR's, and visual approaches."
            ],
            "correct": "DP's, STAR's, and visual approaches."
        },
        {
            "question": "What is the significance of an ATC clearance which reads '...CRUISE SIX THOUSAND...'?",
            "choices": [
                "It authorizes a pilot to conduct flight at any altitude from minimum IFR altitude up to and including 6,000.",
                "The pilot must maintain 6,000 until reaching the IAF serving the destination airport, then execute the published approach procedure.",
                "The pilot is authorized to conduct flight at any altitude from minimum IFR altitude up to and including 6,000, but each change in altitude must be reported to ATC."
            ],
            "correct": "It authorizes a pilot to conduct flight at any altitude from minimum IFR altitude up to and including 6,000."
        },
        {
            "question": "Which ATC clearance should instrument rated pilots request in order to climb through a cloud layer or an area of reduced visibility and then continue the flight VFR?",
            "choices": [
                "Special VFR to VFR Over the Top.",
                "To VFR on Top.",
                "VFR Over the Top."
            ],
            "correct": "To VFR on Top."
        },
        {
            "question": "Which report should be made to ATC without a specific request when not in radar contact?",
            "choices": [
                "When leaving final approach fix inbound on final approach.",
                "Entering instrument meteorological conditions.",
                "Correcting an E.T.A. any time a previous E.T.A. is in error in excess of 2 minutes."
            ],
            "correct": "When leaving final approach fix in bound on final approach."
        },
        {
            "question": "A 'CRUISE FOUR THOUSAND FEET' clearance would mean that the pilot is authorized to:",
            "choices": [
                "Vacate 4,000 feet without notifying ATC.",
                "Climb to, but not descend from 4,000 feet, without further ATC clearance.",
                "Use any altitude from minimum IFR to 4,000 feet, but must report leaving each altitude."
            ],
            "correct": "vacate 4,000 feet without notifying ATC."
        },
        {
            "question": "An abbreviated departure clearance '...CLEARED AS FILED...' will always contain the name:",
            "choices": [
                "And number of the STAR to be flown when filed in the flight plan.",
                "Of the destination airport filed in the flight plan.",
                "Of the first compulsory reporting point if not in a radar environment."
            ],
            "correct": "of the destination airport filed in the flight plan."
        },
        {
            "question": "How is your flight plan closed when your destination airport has IFR conditions and there is no control tower or flight service station (FSS) on the field?",
            "choices": [
                "The ARTCC controller will close your flight plan when you report the runway in sight.",
                "You may close your flight plan any time after starting the approach by contacting any FSS or ATC facility.",
                "Upon landing, you must close your flight plan by radio or by telephone to any FSS or ATC facility."
            ],
            "correct": "Upon landing, you must close your flight plan by radio or by telephone to any FSS or ATC facility."
        },
        {
            "question": "For which speed variation should you notify ATC?",
            "choices": [
                "When the groundspeed changes more than 5 knots.",
                "When the average true airspeed changes 5 percent or 10 knots, whichever is greater.",
                "Any time the groundspeed changes 10 MPH."
            ],
            "correct": "When the average true airspeed changes 5 percent or 10 knots, whichever is greater."
        },
        {
            "question": "For IFR planning purposes, what are the compulsory reporting points when using VOR/DME or VORTAC fixes to define a direct route not on established airways?",
            "choices": [
                "Fixes selected to define the route.",
                "There are no compulsory reporting points unless advised by ATC.",
                "At the changeover points."
            ],
            "correct": "Fixes selected to define the route."
        },
        {
            "question": "When may a pilot cancel the IFR flight plan prior to completing the flight?",
            "choices": [
                "Only in VFR conditions outside positive controlled airspace.",
                "Any time.",
                "Only if an emergency occurs."
            ],
            "correct": "Only in VFR conditions outside positive controlled airspace."
        },
        {
            "question": "What does declaring 'minimum fuel' to ATC imply?",
            "choices": [
                "Merely an advisory that indicates an emergency situation is possible should any undue delay occur.",
                "Traffic priority is needed to the destination airport.",
                "Emergency handling is required to the nearest useable airport."
            ],
            "correct": "Merely an advisory that indicates an emergency situation is possible should any undue delay occur."
        },
        {
            "question": "During an IFR flight in IMC, a distress condition is encountered (fire, mechanical, or structural failure). The pilot should:",
            "choices": [
                "Not hesitate to declare an emergency and obtain an amended clearance.",
                "Wait until the situation is immediately perilous before declaring an emergency.",
                "Contact ATC and advise that an urgency condition exists and request priority consideration."
            ],
            "correct": "not hesitate to declare an emergency and obtain an amended clearance."
        },
        {
            "question": "When should your transponder be on Mode C while on an IFR flight?",
            "choices": [
                "When passing 12,500 feet MSL.",
                "Only when ATC requests Mode C.",
                "At all times if the equipment has been calibrated, unless requested otherwise by ATC."
            ],
            "correct": "At all times if the equipment has been calibrated, unless requested otherwise by ATC."
        },
        {
            "question": "When setting the altimeter, pilots should disregard:",
            "choices": [
                "Effects of nonstandard atmospheric temperatures and pressures.",
                "The mechanical variance errors of the standby instrument.",
                "Ground calibration offsets below 1,000 feet field elevation."
            ],
            "correct": "Effects of nonstandard atmospheric temperatures and pressures."
        },
        {
            "question": "When speed adjustment is necessary to maintain separation, what minimum speed may ATC request of a turbine-powered aircraft operating below 10,000 ft?",
            "choices": ["200 knots", "210 knots", "250 knots"],
            "correct": "210 knots"
        },
        {
            "question": "When a speed adjustment is necessary to maintain separation, what minimum speed may ATC request of a turbine-powered aircraft departing an airport?",
            "choices": ["200 knots", "210 knots", "230 knots"],
            "correct": "230 knots"
        },
        {
            "question": "If ATC requests a speed adjustment that is not within the operating limits of the aircraft, what action must a pilot take?",
            "choices": [
                "Comply as closely as safely possible and file a report later.",
                "Accept the instruction and notify the operator upon landing.",
                "Advise ATC of the airspeed that will be used."
            ],
            "correct": "Advice ATC of the airspeed that will be used."
        },
        {
            "question": "Under what condition may a pilot on an IFR flight plan comply with authorization to maintain 'VFR on Top'?",
            "choices": [
                "Maintain instrument altitudes while staying clear of all visually identified clouds.",
                "Maintain VFR altitudes, cloud clearances, and comply with applicable instrument flight rules.",
                "Navigate strictly via visual lookouts while ignoring standard routing fixes."
            ],
            "correct": "Maintain VFR altitudes, cloud clearances, and comply with applicable instrument flight rules."
        },
        {
            "question": "What cloud clearance is authorized when maintaining 'VFR on Top'?",
            "choices": [
                "May maintain VFR clearance above, below, or between layers.",
                "Must stay at least 2,000 feet vertically clear of all layers.",
                "Is limited to clear sky conditions with no structural layers below."
            ],
            "correct": "May maintain VFR clearance above, below, or between layers."
        },
        {
            "question": "In what airspace will ATC not authorize 'VFR on Top'?",
            "choices": ["Class G airspace", "Class E airspace", "Class A airspace"],
            "correct": "Class A airspace"
        },
        {
            "question": "What separation or service by ATC is afforded pilots authorized 'VFR on Top'?",
            "choices": [
                "Standard IFR radar separation from all traffic.",
                "Complete procedural cross-fixing.",
                "Traffic advisories only"
            ],
            "correct": "Traffic advisories only"
        },
        {
            "question": "Which range of transponder codes should a pilot avoid switching through when changing codes to prevent triggering inadvertent alarms?",
            "choices": ["1200 series", "7000 series", "7500, 7600 and 7700 series"],
            "correct": "7500, 7600 and 7700 series"
        },
        {
            "question": "What minimum condition is suggested for declaring an emergency?",
            "choices": [
                "Anytime the pilot is doubtful of a condition that could adversely affect flight safety.",
                "Only when structural airframe loss is mathematically certain.",
                "When usable fuel drops below the 45-minute cruising threshold."
            ],
            "correct": "Anytime the pilot is doubtful of a condition that could adversely affect flight safety."
        },
        {
            "question": "Each pilot who deviates from an ATC clearance in response to a TCAS advisory is expected to do what immediately?",
            "choices": [
                "Request a formal clearance change from approach control.",
                "Maintain the new course permanently until landing.",
                "Notify ATC of the deviation as soon as possible"
            ],
            "correct": "notify ATC of the deviation as soon as possible"
        },
        {
            "question": "Each pilot who deviates from an ATC clearance in response to a TCAS advisory is expected to notify ATC and do what after the conflict is resolved?",
            "choices": [
                "Maintain the deviation altitude until a new clearance is generated.",
                "Proceed directly to the alternate destination airport.",
                "Expeditiously return to the ATC clearance in effect prior to the advisory, after the conflict is resolved."
            ],
            "correct": "Expeditiously return to the ATC clearance in effect prior to the advisory, after the conflict is resolved."
        },

        # --- Flashcard Section ---
        {
            "question": "What cannot be left out from an operational position report?",
            "choices": [],
            "correct": "callsign, position and time"
        },
        {
            "question": "Clearance limit is defined as:",
            "choices": [],
            "correct": "the point to which aircraft is granted ATC clearance"
        },
        {
            "question": "What is the priority level of the message 'LINE UP' relative to other airfield instructions?",
            "choices": [],
            "correct": "same as 'TAXI TO HOLDING POINT RUNWAY 20'"
        },
        {
            "question": "What is the correct and standardized reply to the instruction 'HOLD SHORT AT RUNWAY'?",
            "choices": [],
            "correct": "HOLDING SHORT"
        },
        {
            "question": "What is the standard aeronautical definition of the phrase 'STANDBY'?",
            "choices": [],
            "correct": "wait and I will call you"
        },
        {
            "question": "What single phrase should be used in aeronautical communications when you want to say 'yes'?",
            "choices": [],
            "correct": "affirm"
        },
        {
            "question": "When making a blind transmission due to suspected receiver failure, what procedure must you follow?",
            "choices": [],
            "correct": "transmit the message twice"
        },
        {
            "question": "What standard time format is used universally in aeronautical communications?",
            "choices": [],
            "correct": "UTC"
        },
        {
            "question": "If you are completely unable to contact a station on a designated frequency, what step should be taken?",
            "choices": [],
            "correct": "try a another appropriate frequency"
        },
        {
            "question": "When asking a transmitting station for a repeat of a message, what phrase should you say?",
            "choices": [],
            "correct": "SAY AGAIN"
        },
        {
            "question": "What is the standard call from an aircraft initializing a missed approach?",
            "choices": [],
            "correct": "GOING AROUND"
        },
        {
            "question": "What is the international emergency transponder code for a hijack situation?",
            "choices": [],
            "correct": "7500"
        },
        {
            "question": "It is the responsibility of the pilot and crew to report a near midair collision as a result of proximity of at least what distance?",
            "choices": [],
            "correct": "500 ft or less to another aircraft"
        },
        {
            "question": "What action should a pilot take for a composite flight plan transitioning from IFR to VFR?",
            "choices": [],
            "correct": "The pilots should advise ATC to cancel the IFR portion and contact the nearest FSS to activate the VFR portion"
        },
        {
            "question": "What action should a pilot take for a composite flight plan transitioning from VFR to IFR?",
            "choices": [],
            "correct": "The pilots should close the VFR portion with the nearest FSS and request the IFR clearance at least 5 minutes prior to IFR."
        },
        {
            "question": "What standard aural and visual indications should be observed over an ILS inner marker position?",
            "choices": [],
            "correct": "Continuous dots at the rate of six per second"
        }
    ]
}

# ==========================================
# INITIALIZATION
# ==========================================

if "initialized" not in st.session_state:
    st.session_state.current_pool = []
    st.session_state.original_set = []  # <--- ADD THIS LINE
    st.session_state.q_idx = 0
    st.session_state.correct_count = 0
    st.session_state.incorrect_pool = []
    st.session_state.round_num = 1
    st.session_state.answered = False
    st.session_state.revealed = False  
    st.session_state.selected_option = None
    st.session_state.shuffled_choices = []
    st.session_state.initialized = True
st.set_page_config(page_title="ATPL Multi-Subject Study Engine", page_icon="✈️", layout="centered")
st.title("📚 ATPL Multi-Subject Study Core")
st.sidebar.header("🛠️ Quiz Configuration")

subject_options = ["All Subjects"] + list(MASTER_QUESTION_BANK.keys())
selected_subject = st.sidebar.selectbox("Select Subject Focus:", subject_options)

if selected_subject == "All Subjects":
    total_available = sum(len(qs) for qs in MASTER_QUESTION_BANK.values())
else:
    total_available = len(MASTER_QUESTION_BANK[selected_subject])

max_questions = st.sidebar.slider("Number of questions:", min_value=1, max_value=max(1, total_available), value=min(20, max(1, total_available)))

if st.sidebar.button("Generate Session / Reset Exam") or not st.session_state.current_pool:
    compiled_pool = []
    if selected_subject == "All Subjects":
        for subject, questions in MASTER_QUESTION_BANK.items():
            for q in questions:
                q_copy = q.copy()
                q_copy["subject_origin"] = subject
                compiled_pool.append(q_copy)
    else:
        for q in MASTER_QUESTION_BANK[selected_subject]:
            q_copy = q.copy()
            q_copy["subject_origin"] = selected_subject
            compiled_pool.append(q_copy)
            
    random.shuffle(compiled_pool)
    st.session_state.current_pool = compiled_pool[:max_questions]
    st.session_state.original_set = st.session_state.current_pool.copy()  # <--- ADD THIS LINE
    st.session_state.q_idx = 0
    st.session_state.correct_count = 0
    st.session_state.incorrect_pool = []
    st.session_state.round_num = 1
    st.session_state.answered = False
    st.session_state.revealed = False
    st.session_state.selected_option = None
    st.session_state.shuffled_choices = []
    st.rerun()

total_in_round = len(st.session_state.current_pool)

if total_in_round > 0:
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Current Score Tally", value=f"{st.session_state.correct_count} / {st.session_state.q_idx}")
    with col2:
        running_pct = (st.session_state.correct_count / st.session_state.q_idx * 100) if st.session_state.q_idx > 0 else 0
        st.metric(label="Current Accuracy Rate", value=f"{running_pct:.1f}%")
        
    st.caption(f"Round {st.session_state.round_num} • Remaining items in active queue: {total_in_round - st.session_state.q_idx}")
    st.write("---")

# ==========================================
# MAIN STUDY ENGINE
# ==========================================
if st.session_state.q_idx < total_in_round:
    q_data = st.session_state.current_pool[st.session_state.q_idx]
    
    st.subheader(f"Question {st.session_state.q_idx + 1} of {total_in_round}")
    st.markdown(f"🏷️ **Subject Area:** `{q_data['subject_origin']}`")
    st.write(q_data['question'])
    
    is_flashcard = len(q_data.get('choices', [])) == 0

    if is_flashcard:
        # --- FLASHCARD UI LOGIC ---
        if not st.session_state.revealed:
            if st.button("Reveal Answer", type="primary"):
                st.session_state.revealed = True
                st.rerun()
        else:
            st.info(f"👉 **Correct Target Answer:** {q_data['correct']}")
            
            eval_col1, eval_col2 = st.columns(2)
            with eval_col1:
                if st.button("👍 Correct", use_container_width=True):
                    st.session_state.correct_count += 1
                    st.session_state.q_idx += 1
                    st.session_state.revealed = False
                    st.rerun()
            with eval_col2:
                if st.button("👎 Wrong", use_container_width=True):
                    st.session_state.incorrect_pool.append(q_data)
                    st.session_state.q_idx += 1
                    st.session_state.revealed = False
                    st.rerun()
    else:
        # --- ORIGINAL MULTIPLE CHOICE UI LOGIC ---
        if not st.session_state.answered and len(st.session_state.shuffled_choices) == 0:
            st.session_state.shuffled_choices = q_data['choices'].copy()
            random.shuffle(st.session_state.shuffled_choices)
            
        user_selection = st.radio(
            "Choose the correct option:",
            st.session_state.shuffled_choices,
            index=None if st.session_state.selected_option is None else st.session_state.shuffled_choices.index(st.session_state.selected_option),
            disabled=st.session_state.answered
        )
        st.session_state.selected_option = user_selection

        if not st.session_state.answered:
            if st.button("Submit Answer", type="primary", disabled=(user_selection is None)):
                st.session_state.answered = True
                st.rerun()
        else:
            if st.session_state.selected_option == q_data['correct']:
                st.success("✨ Correct!")
            else:
                st.error(f"❌ Incorrect.")
                st.info(f"👉 Correct target answer: **{q_data['correct']}**")
                
            if st.button("Next Question"):
                if st.session_state.selected_option == q_data['correct']:
                    st.session_state.correct_count += 1
                else:
                    st.session_state.incorrect_pool.append(q_data)
                    
                st.session_state.q_idx += 1
                st.session_state.answered = False
                st.session_state.selected_option = None
                st.session_state.shuffled_choices = []
                st.rerun()
else:
    # ==========================================
    # SESSION OVER / SPACED REPETITION ENGINE
    # ==========================================
    score_percentage = (st.session_state.correct_count / total_in_round) * 100 if total_in_round > 0 else 100
    st.success("🎉 Exam Configuration Block Finalized!")
    st.metric(label="Final Exam Score", value=f"{st.session_state.correct_count} / {total_in_round}", delta=f"{score_percentage:.1f}%")
    
    # Create side-by-side action buttons
    end_col1, end_col2 = st.columns(2)
    
    with end_col1:
        if st.button("🔄 Repeat Current Set", use_container_width=True):
            st.session_state.current_pool = st.session_state.original_set.copy()
            st.session_state.q_idx = 0
            st.session_state.correct_count = 0
            st.session_state.incorrect_pool = []
            st.session_state.round_num = 1
            st.session_state.answered = False
            st.session_state.revealed = False
            st.session_state.selected_option = None
            st.session_state.shuffled_choices = []
            st.rerun()
            
    with end_col2:
        if st.session_state.incorrect_pool:
            if st.button("🔁 Spaced-Repetition Pass", use_container_width=True):
                st.session_state.current_pool = st.session_state.incorrect_pool.copy()
                random.shuffle(st.session_state.current_pool)
                st.session_state.incorrect_pool = []
                st.session_state.q_idx = 0
                st.session_state.correct_count = 0
                st.session_state.round_num += 1
                st.session_state.answered = False
                st.session_state.revealed = False
                st.session_state.selected_option = None
                st.session_state.shuffled_choices = []
                st.rerun()
        else:
            if st.button("🧹 Clear & Reset Engine", use_container_width=True):
                st.session_state.clear()
                st.rerun()
                
    if st.session_state.incorrect_pool:
        st.warning(f"Review Core: {len(st.session_state.incorrect_pool)} missed item sequences require correction.")
    else:
        st.balloons()
        st.write("### 💯 Absolute Subject Mastery Confirmed!")
