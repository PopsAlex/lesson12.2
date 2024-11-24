import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        ciferka = 1
        distances = {}
        quantity = len(self.participants)
        while self.participants:
            for participant in self.participants:
                if participant.distance >= self.full_distance:
                    participant.distance += ciferka
                    ciferka -= 1
                    distances[participant.distance] = participant
                    if len(distances) == quantity:
                        list_distance = []
                        for i in distances.keys():
                            list_distance.append(i)
                        for j in sorted(list_distance, reverse=True):
                            finishers[place] = str(distances[j])
                            place += 1
                    self.participants.remove(participant)
                    continue
                participant.run()
        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.useyn = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        for i in self.all_results:
            print(i)

    def test_race_first(self):
        tour = Tournament(90, self.useyn, self.nick)
        start = tour.start()
        self.all_results = start
        self.assertTrue(self.all_results[len(self.all_results)] == 'Ник', f'Должен быть Ник')
        print(self.all_results)

    def test_race_second(self):
        tour = Tournament(90, self.andrey, self.nick)
        start = tour.start()
        self.all_results = start
        self.assertTrue(self.all_results[len(self.all_results)] == 'Ник', 'Должен быть Ник')
        print(self.all_results)

    def test_race_third(self):
        tour = Tournament(90, self.useyn, self.andrey, self.nick)
        start = tour.start()
        self.all_results = start
        self.assertTrue(self.all_results[len(self.all_results)] == 'Ник', 'Должен быть Ник')
        print(self.all_results)

    def test_race_additional_first(self):
        tour = Tournament(90, self.andrey, self.useyn)
        start = tour.start()
        self.all_results = start
        self.assertTrue(self.all_results[len(self.all_results)] == 'Андрей', 'Должен быть Андрей')
        # print(f'Доп.тест: {self.all_results}')

    def test_race_additional_second(self):
        tour = Tournament(90, self.useyn, self.andrey,)
        start = tour.start()
        self.all_results = start
        self.assertTrue(self.all_results[len(self.all_results)] == 'Андрей', 'Должен быть Андрей')
        # print(f'Доп.тест: {self.all_results}')


if __name__ == '__main__':
    unittest.main()
