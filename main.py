import json
import os
import signal
import sys

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
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.quizzes = data.get('quizzes', [])
                    self.score = data.get('score', 0)
            except json.JSONDecodeError:
                self.init_default_quizzes()
        else:
            self.init_default_quizzes()

    def init_default_quizzes(self):
        self.quizzes = [
            {"question": "백상아리가 물 밖으로 뛰어오르는 행동은?", "choices": ["브레싱", "브리칭", "스파이호핑", "루트파인딩"], "answer": 2},
            {"question": "백상아리가 전기장을 감지하는 기관은?", "choices": ["로렌스기관", "라이어트기관", "로렌치니기관", "레미아기관"], "answer": 3},
            {"question": "백상아리가 에너지를 비축하는 기관은?", "choices": ["심장", "위", "대장", "간"], "answer": 4},
            {"question": "백상아리의 천적은?", "choices": ["물개", "범고래", "해파리", "북극곰"], "answer": 2},
            {"question": "백상아리의 멸종위기등급은?", "choices": ["CR(절멸 위급)", "EN(절멸 위기)", "VU(취약)", "NT(준위협)"], "answer": 3}
        ]
        self.save_data()

    def save_data(self):
        """데이터 동기화 전략: 파일 저장 보장"""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump({"quizzes": self.quizzes, "score": self.score}, f, ensure_ascii=False, indent=4)

    # 3. 메뉴별 기능 구현
    def play_quiz(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        print("\n--- 퀴즈 시작 ---")
        for q in self.quizzes:
            print(f"\n문제: {q['question']}")
            for i, choice in enumerate(q['choices'], 1):
                print(f"{i}) {choice}")

            num_choices = len(q['choices'])
            while True:
                try:
                    ans = int(input(f"정답 번호: ").strip())
                    if 1 <= ans <= num_choices:
                        break
                    print(f"1부터 {num_choices} 사이의 번호를 입력해주세요.")
                except ValueError:
                    print("숫자만 입력해주세요.")

            if ans == q['answer']:
                print("정답입니다! (+10점)")
                self.score += 10
            else:
                print(f"틀렸습니다. 정답은 {q['answer']}번입니다.")
        
        self.save_data()

    def add_quiz(self):
        print("\n--- 새 퀴즈 추가 ---")
        
        while True:
            q = input("새 문제 내용: ").strip()
            if q:
                break
            print("문제 내용을 입력해주세요.")

        c = []
        for i in range(1, 5):
            while True:
                choice_text = input(f"보기 {i}: ").strip()
                if choice_text:
                    c.append(choice_text)
                    break
                print(f"보기 {i}의 내용을 입력해주세요.")

        while True:
            try:
                a = int(input("정답 번호: ").strip())
                if 1 <= a <= 4:
                    break
                print("1에서 4 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("숫자만 입력해주세요.")

        self.quizzes.append({"question": q, "choices": c, "answer": a})
        self.save_data()
        print("퀴즈가 성공적으로 추가되었습니다!")

    def list_quizzes(self):
        print("\n--- 퀴즈 목록 ---")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q['question']}")

    def show_score(self):
        print(f"\n현재 누적 점수: {self.score}점")

    # [보완] 안전한 종료 및 데이터 동기화
    def shutdown(self):
        print("\n데이터를 동기화(저장)한 후 안전하게 프로그램을 종료합니다.")
        self.save_data()
        print("게임을 종료합니다.")
        sys.exit(0)

# 4. 시그널 처리 및 메뉴 선택 시스템
if __name__ == "__main__":
    game = QuizGame()

    # [보완] 강제종료 시그널(Ctrl+C SIGINT, SIGTERM) 핸들러 등록
    def signal_handler(sig, frame):
        print("\n\n[경고] 프로그램 강제 종료 시그널(SIGINT)이 감지되었습니다.")
        game.shutdown()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while True:
        try:
            print("\n[ 퀴즈 게임 메뉴 ]")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 현재 점수 확인")
            print("5. 종료")

            choice = input("메뉴 선택: ").strip()
            if choice == '1': game.play_quiz()
            elif choice == '2': game.add_quiz()
            elif choice == '3': game.list_quizzes()
            elif choice == '4': game.show_score()
            elif choice == '5':
                game.shutdown()
                break
            else: print("잘못된 입력입니다.")
        except KeyboardInterrupt:
            signal_handler(None, None)
