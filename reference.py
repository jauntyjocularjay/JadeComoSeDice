from enum import Enum



D20_BASE = 'https://github.com/jauntyjocularjay/D20Resources/tree/master'
README = 'readme'
LINK = 'link'
FUTURED20 = 'FutureD20'
CYBERNETICS = 'cybernetics'
ROLES= 'roles'
AMBASSADOR = 'Ambassador'
DOGFIGHTER = 'Dogfighter'
DREADNOUGHT = 'Dreadnought'
ENGINEER = 'Engineer'
EXPLORER = 'Explorer'
FIELD_OFFICER = 'FieldOfficer'
HELIX_WARRIOR = 'HelixWarrior'
MECHA_JOCKEY = 'MechaJockey'
SPACE_MONKEY = 'SpaceMonkey'
SWINDLER = 'Swindler'
TECHNOSAVANT = 'Technosavant'
TRACER = 'Tracer'
XENOPHILE = 'Xenophile'

D20 = {
    FUTURED20: {
        ROLES: {
            AMBASSADOR: f'{D20_BASE}/FutureD20/Classes/Ambassador.md',
            DOGFIGHTER: f'{D20_BASE}/FutureD20/Classes/Dogfighter.md',
            DREADNOUGHT: f'{D20_BASE}/FutureD20/Classes/Dreadnought.md',
            ENGINEER: f'{D20_BASE}/FutureD20/Classes/Engineer.md',
            EXPLORER: f'{D20_BASE}/FutureD20/Classes/Explorer.md',
            FIELD_OFFICER: f'{D20_BASE}/FutureD20/Classes/FieldOfficer.md',
            HELIX_WARRIOR: f'{D20_BASE}/FutureD20/Classes/HelixWarrior.md',
            MECHA_JOCKEY: f'{D20_BASE}/FutureD20/Classes/MechaJockey.md',
            SPACE_MONKEY: f'{D20_BASE}/FutureD20/Classes/SpaceMonkey.md',
            SWINDLER: f'{D20_BASE}/FutureD20/Classes/Swindler.md',
            TECHNOSAVANT: f'{D20_BASE}/FutureD20/Classes/Technosavant.md',
            TRACER: f'{D20_BASE}/FutureD20/Classes/Tracer.md',
            XENOPHILE: f'{D20_BASE}/FutureD20/Classes/Xenophile.md'
        }
    }
}

class Page(Enum):
    FUTURED20 = f'{D20_BASE}/FutureD20'
    CYBERNETICS = f'{D20_BASE}/FutureD20/Cybernetics'
    ROLES = f'{D20_BASE}/FutureD20/Classes'

class Role(Enum):
    AMBASSADOR = f'{D20_BASE}/FutureD20/Classes/Ambassador.md'
    DOGFIGHTER = f'{D20_BASE}FutureD20/Classes/Dogfighter.md'
    DREADNOUGHT = f'{D20_BASE}FutureD20/Classes/Dreadnought.md'
    ENGINEER = f'{D20_BASE}FutureD20/Classes/Engineer.md'
    EXPLORER = f'{D20_BASE}FutureD20/Classes/Explorer.md'
    FIELD_OFFICER = f'{D20_BASE}FutureD20/Classes/FieldOfficer.md'
    HELIX_WARRIOR = f'{D20_BASE}FutureD20/Classes/HelixWarrior.md'
    MECHA_JOCKEY = f'{D20_BASE}FutureD20/Classes/MechaJockey.md'
    SPACE_MONKEY = f'{D20_BASE}FutureD20/Classes/SpaceMonkey.md'
    SWINDLER = f'{D20_BASE}FutureD20/Classes/Swindler.md'
    TECHNOSAVANT = f'{D20_BASE}FutureD20/Classes/Technosavant.md'
    TRACER = f'{D20_BASE}FutureD20/Classes/Tracer.md'
    XENOPHILE = f'{D20_BASE}FutureD20/Classes/Xenophile.md'