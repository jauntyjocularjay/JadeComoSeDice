# Jade's D20 Reference Bot

A quick-reference Discord bot for D20 classes, skills, equipment, cybernetics, mutations, and dice rolls.

## Getting Started

Use `//` before each command.

Examples:

```text
//roll 2d6
//role fighter
//skill stealth
//equipment
```

Commands are case-insensitive, so `//ROLL`, `//Role`, and `//SKILL` all work.

## Commands

### Tutorial

`//tutorial`

Send the user guide directly to your DMs.

Aliases:

```text
//how
//faq
```

### Dice

`//roll [dice]`

Roll one or more dice.

Examples:

```text
//roll 2d6
//roll 2d6, 4d20
```

You can also use `//Roll` or `//ROLL`.

### Role lookup

`//role [name]`

Look up a class or role by name.

Examples:

```text
//role fighter
//class hacker
```

You can also use:

```text
//roles
//classes
```

These show the available role categories and reference links.

### Equipment

`//equipment`

Open the Future D20 equipment reference.

Aliases:

```text
//equip
//gear
```

### Cybernetics

`//cybernetics`

Open the Future D20 cybernetics reference.

Aliases:

```text
//aug
//augmentation
//augmentations
//cybernetic
```

### Skill lookup

`//skill [name]`

Look up a skill by name.

Examples:

```text
//skill stealth
//skills
```

Aliases:

```text
//Skills
```

### Bestiary lookup

`//beast [name]`

Look up a creature or bestiary entry.

Aliases:

```text
//beasts
//animal
//animals
```

### Mutation lookup

`//mutation [name]`

Look up a mutation by name.

Alias:

```text
//mutations
```

## Quick Tips

- Start with `//` for every command.
- Use partial names when searching; the bot looks for matching entries.
- For role and skill lookup, shorter searches may match multiple results, and the first match is returned.
- If you want a reference link without a search term, use commands like `//roles` or `//skills`.

