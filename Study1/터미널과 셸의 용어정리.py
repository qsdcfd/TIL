#!/usr/bin/env python
# coding: utf-8

# echo:뒤이어 입력한 내용 출력
# ~: Home 디렉토리
# pwd: 현재 위치 출력
# ls:디렉토니 내의 모든 파일 출력
# ls -l: 자세한 정보 출력
# ls --all:숨긴 것까지 출력
# ls .폴더명: 숨긴 거 출력
# ls -h:파일 크기를 알아볼 수 있는 단위
# ls -t: 파일 수정시간 순으로 정렬해서 출력
# ls -r: 정렬 순서 뒤집어서 출력
# .:현재폴더
# ..:상위폴더
# cd:디렉토리 변경
# mkdir: 디렉토리 생성
# rm -r: 싹다 삭제
# rm: 일반 파일만 삭제
# cp:폴더 복사
# ps: 현재 터미널과 관련된 프로세스 목록 출력
# ps -ef:부가정보 출력
# PID: process ID번호
# TTY: 터미널
# 패키지: 특정기능을 하는 프로그램
# apt-get: 패키지 실행
# APT:패키지 관리자
# sudo:프로그램 구동.(최고 관리자 권한)
# sudo apt list --installed | grep (패키지명) : 원하는 패키지만 검색.
# cat:하나 이상의 텍스트 파일을 순서대로 출력
# chown: 소유 사용자와 그룹을 변경
# chmod:대상 파일의 권한을 변경
# grep: 특정 문자열을 포함한 라인만 선택 출력
# kill:PID에 해당하는 프로세스에 시그널 보냄
# which:명령어의 전체 경로 출력
# history:셸 명령어 이력 출력
# man: 프로그램의 매뉴얼 페이지 출력
# env: 명령어 제공x, 현재 환경의 정보 출력
# less: 조회 및 검색
# head: 앞 몇 줄만 출력
# tail: 마지막 몇 줄만 출력
# cut: 텍스트를 구분자에 따라 나눕니다
# uniq:중복값 제거
# wc:단위 세기
# comm: txt파일 비교
# zcat:압축된 txt파일 출력
# sed:정규식-->txt변형
# awk: 텍스트 스캔 및 변형
# ln: 파일 링크 생성
# touch:수정시간 변경
# tar:통합 및 압축
# mount:파일 시스템 추가
# df:남은  용량 표시
# fg:전경 가져오기
# bg:배경 보내기
# jobs: 작업 목록 표시
# ssh:원격
# tmux:셸 세션 유지
# watch: 명령을 주기적 실행
# curl: URL과 통신
# wget:파일 다운로드
# scp:SSH를 통해 원격 전송
# ssh-keygen:SSH공개키 비밀키 쌍으로 생성
# sort:입력된 텍스트를 줄 단위로 정렬
# export:셸의 변수나 함수를 현재 환경으로 내보냅니다
# env:명령어가 제공되지 않은 경우 현재 환경의 정보 출력
# $: 환경 변수로 OS가 프로세스 단위로 사용하는 변수
# 상대경로: 내가 현재있는 디렉토리에 영향을 받는 위치
# 절대 경로: 똑같은 곳을 가리키기 위해 전체 적음
# 커널: 통합관리 및 분배
# GUI셸:다른 종류의 프로그램들과 함께 사용
# CLI:편의기능을 덧붙인 bash가 설치되어 있음
# OS가 프로세스 단위로 메모리와 CPU연산등 분배 및 관리
# 메모리 관리:가상 메모리 일부만 떼어냄
# CPU자원 관리: 스레드 단위로 코어 하나씩 사용. 다다익선
# 가상화: 실제 물리적 서버(host), 가상서버(guest)
# 도커: 컨테이너 가상화를 손쉽게 제공
