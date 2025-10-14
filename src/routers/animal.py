from fastapi import APIRouter

router = APIRouter(prefix='/animal')

animals = [
    {
        'title': 'котик'
    },
    {
        'title': 'австралийский динго'
    },
    {
        'title': 'Огненный дракон'
    },
    {
        'title': 'Ядовитый дракон'
    },
    {
        'title': 'Болотная тварь'
    },
    {
        'title': 'Оборотень'
    }
]


@router.get('/list')
async def get_animals_list():
    return animals 


@router.get('/{animal_position}')
async def get_animal(animal_position: int):
    return animals[animal_position]