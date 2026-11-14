import json
import os
import random
import signal
import sys


class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return self.answer == user_answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["question"], data["choices"], data["answer"])


class QuizGame:
    def __init__(self):
        self.file_path = 'state.json'
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    raw_quizzes = data.get('quizzes', [])
                    self.quizzes = [Quiz.from_dict(q) for q in raw_quizzes]
                    self.best_score = data.get('best_score', data.get('score', 0))
            except (json.JSONDecodeError, KeyError):
                self.init_default_quizzes()
        else:
            self.init_default_quizzes()

    def init_default_quizzes(self):
        self.quizzes = [
            Quiz("백상아리가 물 밖으로 뛰어오르는 행동은?", ["브레싱", "브리칭", "스파이호핑", "루트파인딩"], 2),
            Quiz("백상아리가 전기장을 감지하는 기관은?", ["로렌스기관", "라이어트기관", "로렌치니기관", "레미아기관"], 3),
            Quiz("백상아리가 에너지를 비축하는 기관은?", ["심장", "위", "대장", "간"], 4),
            Quiz("백상아리의 천적은?", ["물개", "범고래", "해파리", "북극곰"], 2),
            Quiz("백상아리의 멸종위기등급은?", ["CR(절멸 위급)", "EN(절멸 위기)", "VU(취약)", "NT(준위협)"], 3)
        ]
        self.best_score = 0
        self.save_data()

    def save_data(self):
        quiz_dicts = [q.to_dict() for q in self.quizzes]
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump({"quizzes": quiz_dicts, "best_score": self.best_score}, f, ensure_ascii=False, indent=4)

    def play_quiz(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        print("\n--- 퀴즈 시작 (랜덤 출제) ---")
        shuffled_quizzes = random.sample(self.quizzes, len(self.quizzes))
        total_questions = len(shuffled_quizzes)
        correct_count = 0

        for idx, q in enumerate(shuffled_quizzes, 1):
            print(f"\n[문제 {idx}/{total_questions}] {q.question}")
            for i, choice in enumerate(q.choices, 1):
                print(f"{i}) {choice}")

            num_choices = len(q.choices)
            while True:
                try:
                    ans = int(input(f"정답 번호 (1-{num_choices}): ").strip())
                    if 1 <= ans <= num_choices:
                        break
                    print(f"1부터 {num_choices} 사이의 번호를 입력해주세요.")
                except ValueError:
                    print("숫자만 입력해주세요.")

            if q.check_answer(ans):
                print("정답입니다! (+10점)")
                correct_count += 1
            else:
                print(f"틀렸습니다. 정답은 {q.answer}번입니다.")

        round_score = correct_count * 10
        print("\n--- 퀴즈 결과 ---")
        print(f"총 {total_questions}문제 중 {correct_count}문제를 맞혔습니다! (이번 점수: {round_score}점)")

        if round_score > self.best_score:
            print(f"🎉 신기록 달성! 최고 점수가 갱신되었습니다. ({self.best_score}점 -> {round_score}점)")
            self.best_score = round_score
        else:
            print(f"현재 최고 점수: {self.best_score}점")

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
                a = int(input("정답 번호 (1-4): ").strip())
                if 1 <= a <= 4:
                    break
                print("1에서 4 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("숫자만 입력해주세요.")

        self.quizzes.append(Quiz(q, c, a))
        self.save_data()
        print("퀴즈가 성공적으로 추가되었습니다!")

    def list_quizzes(self):
        print("\n--- 퀴즈 목록 ---")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q.question}")

    def show_score(self):
        if self.best_score == 0:
            print("\n아직 기록된 최고 점수가 없습니다. '1. 퀴즈 풀기'를 통해 첫 기록을 세워보세요!")
        else:
            print(f"\n역대 최고 점수: {self.best_score}점")

    def shutdown(self):
        print("\n데이터를 저장한 후 안전하게 프로그램을 종료합니다.")
        self.save_data()
        print("게임을 종료합니다.")
        sys.exit(0)


if __name__ == "__main__":
    game = QuizGame()

    def signal_handler(sig, frame):
        print("\n\n[경고] 프로그램 강제 종료 시그널이 감지되었습니다.")
        game.shutdown()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while True:
        try:
            print("\n[ 퀴즈 게임 메뉴 ]")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 최고 점수 확인")
            print("5. 종료")

            choice = input("메뉴 선택: ").strip()
            if choice == '1': game.play_quiz()
            elif choice == '2': game.add_quiz()
            elif choice == '3': game.list_quizzes()
            elif choice == '4': game.show_score()
            elif choice == '5': game.shutdown()
            else: print("잘못된 입력입니다. 1~5 사이의 번호를 선택해주세요.")
        except KeyboardInterrupt:
            signal_handler(None, None)
