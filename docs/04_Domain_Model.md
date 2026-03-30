# Domain Model

## 1. Overview

This domain model shows the main concepts of the RoomLight system and how they relate to each other. The goal of this model is to help with the design before writing code.

---

## 2. Requirements → Nouns

| Requirement                                                                                                 | Nouns found                       |
| ----------------------------------------------------------------------------------------------------------- | --------------------------------- |
| 001 - The system allows creation of predefined lighting modes                                               | system, lighting modes            |
| 002 - A lighting mode can be applied to single room                                                         | lighting mode, room               |
| 003 - The system allows configuring lighting settings once and synchronizing them across all selected rooms | system, lighting settings, rooms  |
| 004 - The system allows grouping of similar room types                                                      | system, room types                |
| 005 - Guests can view the current lighting mode of their room                                               | guests, lighting mode, room       |
| 006 - Allows customization of an existing lighting mode                                                     | lighting mode                     |
| 008 - System acknowledges abnormal situations such as fire alarms and changes lighting mode accordingly     | system, fire alarm, lighting mode |
| 011 - System automatically shuts light when room is not booked                                              | system, light, room               |

---

## 3. Domain Concepts

- Room  
- RoomGroup  
- LightMode  
- Guest
- User (Staff)
- SystemEvent (Firealarm etc)
- RoomLight

---
## 4. Domain Model
````

+---------------------+
|  RoomLightSystem    |
+---------------------+
          |
          |
          v
+---------------------+
|     RoomGroup       |
+---------------------+
          |
       contains
          |
          v
+---------------------+
|        Room         |
+---------------------+
     |                |
   viewed by         has
     v                v
+-------------+  +------------------+
|  Guest      |  |   LightMode      |
+-------------+  +------------------+
    ^                               ^
     |                              |
   Modifies                      Affects
     |                              |
+------------------+           +-------------------+
|  User (Staff)    |           |      SystemEvent  |
+------------------+           +-------------------+

```
