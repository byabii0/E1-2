import json
import os

# 1. 클래스(OOP) 사용
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

class QuizGame:
    def __init__(self):
        self.file_path = 'state.json'
        self.quizzes = []
        self.score = 0
        self.load_data() # 시작할 때 파일 불러오기

    # 2. JSON 파일 저장/불러오기
    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.quizzes = data.get('quizzes', [])
                self.score = data.get('score', 0)
        else:
            # 초기 데이터 (파일이 없을 때만 생성)
            self.quizzes = [
                {"question": "사과는 영어로?", "choices": ["Apple", "Banana", "Cherry", "Date"], "answer": 1},
                {"question": "바나나는 무슨 색?", "choices": ["빨강", "노랑", "파랑", "초록"], "answer": 2},
                {"question": "하늘을 나는 새는?", "choices": ["개", "고양이", "독수리", "토끼"], "answer": 3},
                {"question": "대한민국의 수도는?", "choices": ["부산", "인천", "제주", "서울"], "answer": 4},
                {"question": "1 + 1은?", "choices": ["1", "2", "3", "4"], "answer": 2}
            ]
            self.save_data()

    def save_data(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump({"quizzes": self.quizzes, "score": self.score}, f, ensure_ascii=False, indent=4)

    # 3. 메뉴별 기능 구현
    def play_quiz(self):
        print("\n--- 퀴즈 시작 ---")
        for q in self.quizzes:
            print(f"\n문제: {q['question']}")
            for i, choice in enumerate(q['choices'], 1):
                print(f"{i}) {choice}")

            try:
                ans = int(input("정답 번호: "))
                if ans == q['answer']:
                    print("정답입니다! (+10점)")
                    self.score += 10
                else:
                    print(f"틀렸습니다. 정답은 {q['answer']}번입니다.")
            except ValueError:
                print("숫자만 입력해주세요.")
        self.save_data()

    def add_quiz(self):
        q = input("새 문제 내용: ")
        c = [input(f"보기 {i}: ") for i in range(1, 5)]
        a = int(input("정답 번호(1-4): "))
        self.quizzes.append({"question": q, "choices": c, "answer": a})
        self.save_data()
        print("퀴즈가 추가되었습니다!")

    def list_quizzes(self):
        print("\n--- 퀴즈 목록 ---")
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q['question']}")

    def show_score(self):
        print(f"\n현재 누적 점수: {self.score}점")

# 4. 메뉴 선택 시스템 (1~5번)
if __name__ == "__main__":
    game = QuizGame()
    while True:
        print("\n[ 퀴즈 게임 메뉴 ]")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 현재 점수 확인")
        print("5. 종료")

        choice = input("메뉴 선택: ")
        if choice == '1': game.play_quiz()
        elif choice == '2': game.add_quiz()
        elif choice == '3': game.list_quizzes()
        elif choice == '4': game.show_score()
        elif choice == '5':
            print("게임을 종료합니다.")
            break
        else: print("잘못된 입력입니다.")
