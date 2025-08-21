# O3DE Hex Colour Material Generator

## Preparing Colour List
Edit your `materials.txt` with a Hex, Name pair.
```
#000000, Black
#FFFFFF, White
```

## Generating Materials
1. Open bash in folder.
2. Enter `python generate_materials.py` command.

> [!NOTE]
> Requires python installation.

## Customization

- Edit `prefix = ` to change the prefix of the material file.
    - Counts from 000 by default. This assures file order matches the list.

Can be expanded to generate all sorts of material data.
```
"baseColor.factor": 0.5,
"metallic.factor": 1.0,
"roughness.factor": 0.33000001311302185,
"specularF0.enableMultiScatterCompensation": true,
"specularF0.factor": 0.8799999952316284
```
and more I can't find.