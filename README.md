# E1-2

# 프로젝트 개요

📌한 줄 요약

파이썬 객체 지향 문법과 JSON 데이터 관리를 활용해 실전 프로그램을 완성하고, Git으로 개발 전 과정을 기록하며 협업 역량의 기초를 다집니다.

🎯 학습 목표

 파이썬의 객체 지향 프로그래밍(OOP)과 JSON 데이터 관리를 활용해 터미널 기반 퀴즈 게임을 처음부터 끝까지 직접 설계 및 구현함으로써, 단순 문법 지식을 실전 프로그램 완성 능력으로 전환하는 것입니다. 이 과정에서 Git의 브랜치 전략과 버전 관리 프로세스를 체계적으로 경험하여 프로그램의 동작 원리를 깊이 이해하고, 향후 팀 협업을 위한 기술적 토대와 데이터 영속성에 대한 감각을 익힙니다.

✅ 미션 완료 체크리스트

**Python 기초**

- [ ] 변수가 무엇이고, 왜 사용하는지 설명할 수 있다.
- [ ] int, str, bool, list, dict의 차이를 설명할 수 있다.
- [ ] if/elif/else로 조건에 따라 다른 동작을 수행할 수 있다.
- [ ] for와 while의 차이를 설명하고 적절히 선택할 수 있다.
- [ ] 함수를 정의하고, 매개변수와 반환값을 활용할 수 있다.

**클래스와 객체**

- [ ] 클래스가 무엇이고, 왜 사용하는지 설명할 수 있다.
- [ ] __init__ 메서드와 self의 역할을 설명할 수 있다.
- [ ] 클래스의 속성(attribute)과 메서드(method)를 정의하고 활용할 수 있다.

**파일 입출력**

- [ ] 파일을 열고, 읽고, 쓰는 기본 과정을 설명할 수 있다.
- [ ] JSON 형식이 무엇이고, 왜 데이터 저장에 사용하는지 설명할 수 있다.2
- [ ] try/except를 사용하여 오류를 처리할 수 있다.


**Git 기초**

- [ ] Git이 무엇이고 왜 필요한지 설명할 수 있다.
- [ ] init, add, commit, push, pull, checkout, clone이 각각 무엇을 하는지 설명할 수 있다.
- [ ] 브랜치를 생성하고 병합할 수 있다.
- [ ] 원격 저장소를 clone하고, pull로 변경사항을 가져올 수 있다.

# 퀴즈 주제와 선정 이유

퀴즈 주제: 백상아리의 기본적인 생태 정보입니다.

선정 이유: 상어가 나오는 영화와 다큐멘터리를 좋아하기 때문입니다.

# 실행 방법

클래스: Quiz, QuizGame

메서드: load_data(), save_data(), play_quiz(), add_quiz(), list_quizzes(), show_score()



# 기능 목록

퀴즈 풀기, 퀴즈 추가, 퀴즈 목록 보기, 현재 점수 확인, 종료 기능이 있습니다. 한 문제를 맞힐 때마다 10점씩 추가됩니다. 퀴즈를 종료해도 점수는 누적됩니다. 1~5 사이의 숫자를 입력하여 각 기능을 실행할 수 있습니다.

# 파일 구조

my_quiz_project/: 최상위 프로젝트 폴더
main.py: 파이썬 실행 코드 파일
state.json: 퀴즈 데이터 및 점수가 자동 저장되는 파일


# 데이터 파일 설명

파일명: state.json

.json은 JavaScript Object Notation의 약자로, 데이터를 저장하고 주고받을 때 사용하는 표준 텍스트 형식을 의미합니다. 텍스트 파일 형태이므로 메모장으로 열어도 사람이 직접 내용을 확인하고 수정하기 쉽습니다.

파일 역할: 퀴즈 데이터(문제, 보기, 정답)와 플레이어의 누적 점수를 프로그램 종료 후에도 영구적으로 유지하는 데이터 보존(영속성) 파일입니다.

인코딩: UTF-8 (표준 인코딩 지원, 한글(퀴즈 질문, 보기)이 깨지지 않고 안정적으로 보존됩니다.)

# Git 저장소 설정

# 메뉴 기능

# 공통 입력/예외 처리 기준(최소 요구)

**공통 입력 요소**

입력 항목 ㅣ 입력되는 위치 ㅣ 데이터 형식

메뉴 번호 ㅣ 메인 메뉴 화면 (choice) ㅣ 문자열 (str)

정답 번호 ㅣ 퀴즈 풀기 화면 (ans) ㅣ 정수형 (int)

새 문제/보기 ㅣ "퀴즈 추가 화면 (q, c)" ㅣ 문자열 (str)

새 정답 번호 ㅣ 퀴즈 추가 화면 (a) ㅣ 정수형 (int)

**공통 입력 처리 기준**

모든 입력은 터미널 콘솔의 input() 함수를 통해 받으며, 입력받은 데이터를 처리할 때 아래 3가지 규칙을 공통으로 적용합니다.

문자열 입력 받기 (input())

사용자로부터 텍스트 입력을 받아 변수에 저장합니다.

타입 변환 및 예외 검사 (int())

정답 번호나 메뉴 입력 시 숫자로 변환하며, 문자 입력 시 에러가 나지 않도록 try-except로 감쌉니다.

입력값 범위 검증 (Validation)

정답 번호는 1~4번 범위 내인지, 메뉴 번호는 1~5번 범위 내인지 검사합니다.

**예외 입력 요소**

예외 입력 요소 ㅣ 발생 위치 ㅣ 사용자의 예외 입력 행동 ㅣ 발생할 수 있는 에러/문제점

문자/특수문자 입력 ㅣ "play_quiz, add_quiz (정답 번호 입력 시)" ㅣ 숫자가 필요한 곳에 ""abc"", ""#"" 등 입력 ㅣ int() 변환 실패로 ValueError 발생하여 프로그램 강제 종료

범위 밖의 숫자 입력 ㅣ "play_quiz, add_quiz, 메뉴 선택" ㅣ 보기가 1~4번인데 0, 5, -1 등 입력 ㅣ 존재하지 않는 정답 처리 또는 논리적 오류 발생

공백/빈 문자열 입력 ㅣ 모든 input() 창 ㅣ 아무것도 입력하지 않고 Enter만 입력 ㅣ 문제 내용이나 보기가 빈 값("""")으로 저장됨

메뉴 입력 오류 ㅣ 메인 메뉴 (choice) ㅣ 1~5번 이외의 문자/숫자 입력 ㅣ 잘못된 메뉴 선택으로 인한 오작동

**예외 처리 기준**

발생 위치 ㅣ 입력 대상 ㅣ 발생 가능한 예외/상황 ㅣ 처리 기준 및 대응 로직

메인 메뉴 ㅣ 메뉴 번호 (1~5) ㅣ "문자 입력, 범위 밖 숫자(0, 6 등), 공백" ㅣ else 블록에서 ""잘못된 입력입니다."" 출력 후 메뉴 재출력

퀴즈 풀기 ㅣ 정답 번호 ㅣ 문자 입력 (ValueError) ㅣ try-except로 예외를 잡아 오답 처리 및 안내 문구 출력

퀴즈 추가 ㅣ 퀴즈 질문/보기 ㅣ 빈 문자열 (Enter만 입력) ㅣ .strip() 적용 및 공백 시 재입력 유도

퀴즈 추가 ㅣ 정답 번호 ㅣ 문자 입력 또는 1~4 범위를 벗어난 숫자 ㅣ 1 <= ans <= 4 조건 검증 및 예외 발생 시 재입력 루프

JSON 입출력 ㅣ state.json ㅣ "파일 미존재, 파일 손상 (JSONDecodeError)" ㅣ os.path.exists 검사 후 미존재 시 초기 데이터 생성

# Git: README 작성 후 최종 푸시한다.

Git 저장소 설정

  PS C:\Users\kmj04> mkdir quiz_project
  
  
      디렉터리: C:\Users\kmj04
  
  
  Mode                 LastWriteTime         Length Name                                                        
  ----                 -------------         ------ ----                                                        
  d-----      2026-11-08   오후 2:21                quiz_project                                                
  
  
  PS C:\Users\kmj04> cd quiz_project
  PS C:\Users\kmj04\quiz_project> git init
  Initialized empty Git repository in C:/Users/kmj04/quiz_project/.git/
  PS C:\Users\kmj04\quiz_project> git config --global user.name "**"
  PS C:\Users\kmj04\quiz_project> git config --global user.email "**"
  PS C:\Users\kmj04\quiz_project> git config --list
  diff.astextplain.textconv=astextplain
  filter.lfs.clean=git-lfs clean -- %f
  filter.lfs.smudge=git-lfs smudge -- %f
  filter.lfs.process=git-lfs filter-process
  filter.lfs.required=true
  http.sslbackend=schannel
  core.autocrlf=true
  core.fscache=true
  core.symlinks=false
  pull.rebase=false
  credential.helper=manager
  credential.https://dev.azure.com.usehttppath=true
  init.defaultbranch=master
  user.name=**
  user.email=**
  core.repositoryformatversion=0
  core.filemode=false
  core.bare=false
  core.logallrefupdates=true
  core.symlinks=false
  core.ignorecase=true

.gitignore 파일에 파이썬 캐시(__pycache), 파이썬 컴파일 파일(*pyc), 가상환경(venv/), 설정 및 비밀번호(.env), VSCode 설정 폴더(.vscode/)를 입력했습니다.

  __pycache__/
  *pyc
  venv/
  .env
  .vscode/

상태 확인

  PS C:\Users\kmj0403232057\quiz_project> git status
  On branch master
  
  No commits yet
  
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
          .gitignore
  
  nothing added to commit but untracked files present (use "git add" to track)
  PS C:\Users\kmj0403232057\quiz_project> git remote add origin https://github.com/byabii0/E1-2.git
  PS C:\Users\kmj0403232057\quiz_project> git remote -v
  origin  https://github.com/byabii0/E1-2.git (fetch)
  origin  https://github.com/byabii0/E1-2.git (push)
  PS C:\Users\kmj0403232057\quiz_project> git add .
  PS C:\Users\kmj0403232057\quiz_project> git push -u origin main
  Enumerating objects: 6, done.
  Counting objects: 100% (6/6), done.
  Delta compression using up to 24 threads
  Compressing objects: 100% (3/3), done.
  Writing objects: 100% (5/5), 574 bytes | 574.00 KiB/s, done.
  Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
  To https://github.com/byabii0/E1-2.git
     469ef09..e2b9376  main -> main
  branch 'main' set up to track 'origin/main'.

PS C:\Users\kmj0403232057\quiz_project> git commit -m "git 저장소 설정"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

root@GNIA-C202-D03:~/projects/E1-2# git add main.py
root@GNIA-C202-D03:~/projects/E1-2# git commit -m "feat: 퀴즈 추가 기능 개선"
[main 5484aa3] feat: 퀴즈 추가 기능 개선
 Committer: root <root@GNIA-C202-D03.ad.gnia.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 94 insertions(+)
 create mode 100644 main.py
root@GNIA-C202-D03:~/projects/E1-2# git checkout main
Already on 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

root@GNIA-C202-D03:~/projects/E1-2# git branch
* main
root@GNIA-C202-D03:~/projects/E1-2# git checkout -b feature/new-quiz
Switched to a new branch 'feature/new-quiz'
root@GNIA-C202-D03:~/projects/E1-2# git add .
root@GNIA-C202-D03:~/projects/E1-2# git commit -m "feat: 브랜치 테스트를 위한 수정"
[feature/new-quiz 0650cea] feat: 브랜치 테스트를 위한 수정
 Committer: root <root@GNIA-C202-D03.ad.gnia.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 65 insertions(+)
 create mode 100644 state.json
root@GNIA-C202-D03:~/projects/E1-2# git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

git merge 기록
    root@GNIA-C202-D03:~/projects/E1-2# git merge feature/new-quiz
    Updating 5484aa3..0650cea
    Fast-forward
    state.json | 65 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    1 file changed, 65 insertions(+)
    create mode 100644 state.json
    root@GNIA-C202-D03:~/projects/E1-2# git branch
    feature/new-quiz
    * main

git push 기록
    root@GNIA-C202-D03:~/projects/E1-2# git push origin main
    Enumerating objects: 7, done.
    Counting objects: 100% (7/7), done.
    Delta compression using up to 24 threads
    Compressing objects: 100% (6/6), done.
    Writing objects: 100% (6/6), 2.39 KiB | 2.39 MiB/s, done.
    Total 6 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
    remote: Resolving deltas: 100% (1/1), done.
    To https://github.com/byabii0/E1-2.git
    8719b43..0650cea  main -> main