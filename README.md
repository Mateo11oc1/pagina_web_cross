# Página web de seguimiento de ejercicios de Crossfit

## Objetivos

* Consolidar los conocimientos sobre programación y el lenguaje Python y adentrarse en el desarrollo de aplicaciones web usando el framework Django.
* Hacer una aplicación web y consolidar esos conocimientos.
* Fuera de los objetivos:
* Divertirse
* Aprender

## Descripción del proyecto

* Aplicación web de seguimiento de ejercicios de crossfit realizados por una persona, se podrá registrar los avances que la persona realiza en un determinado ejercicio que se escoja. Se podrá consultar un histórico de los avances que se realizan a lo largo del tiempo.
* Se podrá registrar el peso con el que se realizan los ejercicios, el número de repeticiones, el número de rondas y el tiempo durante el que se realizó el ejercicio.

## Modelo de datos

* El modelo de datos se presenta a continuación

```mermaid
---
title: Modelo de datos
---
%%{init: {'theme':'forest' }}%%
erDiagram
USER {
    CharField dni PK
    ForeignKey country FK
    CharField name
    CharField last_name
    EmailField email
    CharField phone
    CharField genre
    DateField date_of_birth
    IntegerField height
    IntegerField weight
    CharField country
    CharField language
    CharField password
}
EXERCISE {
    IntegerField id PK
    ForeignKey type_of_exercise FK
    CharField name
    TextField description
}
TypeOfExercise {
    IntegerField id PK
    CharField name 
    TextField description
}
COUNTRY {
    CharField code PK
    CharField name
}

REGISTER {
    IntegerField id
    ForeignKey user FK
    ForeignKey exercise FK
    IntegerField weight
    IntegerField sets
    IntegerField reps
}

EXERCISE }|--|| TypeOfExercise: has
REGISTER }|--|| USER:has
REGISTER }|--|| EXERCISE:has
COUNTRY ||--|{ USER:live
```
