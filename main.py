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
                {"question": "백상아리가 물 밖으로 뛰어오르는 행동은?", "choices": ["브레싱", "브리칭", "스파이호핑", "루트파인딩"], "answer": 2},
                {"question": "백상아리가 전기장을 감지하는 기관은?", "choices": ["로렌스기관", "라이어트기관", "로렌치니기관", "레미아기관"], "answer": 3},
                {"question": "백상아리가 에너지를 비축하는 기관은?", "choices": ["심장", "위", "대장", "간"], "answer": 4},
                {"question": "백상아리의 천적은?", "choices": ["물개", "범고래", "해파리", "북극곰"], "answer": 2},
                {"question": "백상아리의 멸종위기등급은?", "choices": ["CR(절멸 위급)", "EN(절멸 위기)", "VU(취약)", "NT(준위협)"], "answer": 3}
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
