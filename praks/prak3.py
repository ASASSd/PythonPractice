class C32(object):
    __state = 'A'

    def trash(self):
        statechart = {
            'A': ['B', 0],                   #0: ['A', 'B'],
            'B': ['C', 2],                   #2: ['B', 'C'],
            'C': ['D', 3],                   #3: ['C', 'D'],
            'D': ['F', 5],                   #5: ['D', 'F'],
            'E': ['C', 8]                    #8: ['E', 'C']
        }
        if statechart.get(self.__state):
            lastState = statechart[self.__state][1]
            self.__state = statechart[self.__state][0]
            return lastState
        else:
            raise RuntimeError

    def rev(self):
        statechart = {
            'A': ['D', 1],    #1: ['A', 'D'],
            'D': ['E', 4],    #4: ['D', 'E'],
            'E': ['A', 7],    #7: ['E', 'A']
        }
        if statechart.get(self.__state):
            lastState = statechart[self.__state][1]
            self.__state = statechart[self.__state][0]
            return lastState
        else:
            raise RuntimeError

    def move(self):
        statechart = {
            'E': ['F', 6]
        }
        if statechart.get(self.__state):
            lastState = statechart[self.__state][1]
            self.__state = statechart[self.__state][0]
            return lastState
        else:
            raise RuntimeError
