## Backend

### 1주차

<table>
    <tbody>
        <tr>
            <th>트랙</th>
            <td>BE</td>
        </tr>
        <tr>
            <th>날짜</th>
            <td>'23.05.03</td>
        </tr>
        <tr>
            <th>주제</th>
            <td>Python 객체 지향 프로그래밍</td>
        </tr>
        <tr>
            <th>목표</th>
            <td>
                • 객체 지향 프로그래밍이 무엇인지 이해할 수 있다.<br/>
                • 클래스를 이용한 간단한 프로그램을 구현할 수 있다.<br/>
                • Django의 MVT 패턴에 대해 이해할 수 있다.<br/>
            </td>
        </tr>
        <tr>
            <th rowspan="5">절차</th>
            <td>
                <strong>클래스 구현과 직렬화 예제 </strong><br/>
                • 객체지향 4개 특성<br/>
                • SOLID 원칙<br/>
                <br/>
                예상 소요 시간 : 15min
            </td>
        </tr>
        <tr>
            <td>
                <strong>2. 클래스</strong><br/>
                • 클래스와 객체<br/>
                • Object 클래스 <br/>
                • 생성자, 멤버변수, 메서드<br/>
                • 간단한 미니 게임 만들어보기<br/>
                <br/>
                예상 소요 시간 : 40min
            </td>
        </tr>
        <tr>
            <td>
                <strong>3. 상속</strong><br/>
                • 상속이란<br/>
                • 위에서 만든 클래스 확장<br/>
                <br/>
                예상 소요 시간 : 20min
            </td>
        </tr>
        <tr>
            <td>
                <strong>4. 모듈</strong><br/>
                • 모듈이란<br/>
                • 모듈화<br/>
                <br/>
                예상 소요 시간 : 10min
            </td>
        </tr>
        <tr>
            <td>
                <strong>5. 직렬화/역직렬화</strong><br/>
                • JSON<br/>
                • 직렬화와 역직렬화<br/>
                <br/>
                예상 소요 시간 : 30min
            </td>
        </tr>
        <tr>
            <th>과제</th>
            <td>클래스 구현과 직렬화 예제 </td>
        </tr>
    </tbody>
</table>

### 2주차

<table>
    <tbody>
        <tr>
            <th>트랙</th>
            <td>BE</td>
        </tr>
        <tr>
            <th>날짜</th>
            <td>'23.05.10</td>
        </tr>
        <tr>
            <th>주제</th>
            <td>Django Framework 소개</td>
        </tr>
        <tr>
            <th>목표</th>
            <td>
            • Django 프레임워크의 사용 목적과 구조를 이해할 수 있다.<br/>
            • 간단한 Modeling 작업을 수행할 수 있다.<br/>
            • Django 내에서 Model을 구현할 수 있다.<br/>
            </td>
        </tr>
        <tr>
            <th rowspan="3">절차</th>
            <td>
                <strong>1. What is Django?</strong><br/>
                • 프레임워크란? <br/>
                • Django란? (20min)<br/>
                    &nbsp;&nbsp;&nbsp;
                   - 클라이언트와 Django 프로세스<br/>
                   &nbsp;&nbsp;&nbsp;
                   - 설치 방법 (가상 환경)<br/>
                   &nbsp;&nbsp;&nbsp;
                   - 실행 해보기<br/>
                • Django App 구조<br/>
                <br/>
                예상 소요 시간 : 20min
            </td>
        </tr>
        <tr>
            <td>
                <strong>2. Modeling</strong><br/>
                • 모델<br/>
                    &nbsp;&nbsp;&nbsp;
                   - 필드<br/>
                    &nbsp;&nbsp;&nbsp;
                   - 유저 모델 예제 분석<br/>
                • 연관 관계 매핑<br/>
                    &nbsp;&nbsp;&nbsp;
                   - 일대일, 일대다, 다대다 관계<br/>
                    &nbsp;&nbsp;&nbsp;
                   - pk & fk<br/>
                • 연관 관계 모델링 예제 분석 (15min)<br/>
                • DataBase Setting & Migration (10min)<br/>
                <br/>
                예상 소요 시간 : 30min
            </td>
        </tr>
        <tr>
            <td>
                <strong>3. Admin Page</strong><br/>
                • Django admin<br/>
                • admin page 데이터 저장 내역 확인 <br/>
                <br/>
                예상 소요 시간 : 10min
            </td>
        </tr>
        <tr>
            <th>과제</th>
            <td>자신만의 MBTI 검사 페이지 만들어보기</td>
        </tr>
    </tbody>
</table>

### 3주차

<table>
    <tbody>
        <tr>
            <th>트랙</th>
            <td>BE</td>
        </tr>
        <tr>
            <th>날짜</th>
            <td>'23.05.17</td>
        </tr>
        <tr>
            <th>주제</th>
            <td>Django 아키텍처 이해</td>
        </tr>
        <tr>
            <th>목표</th>
            <td>
            • url 및 뷰 플로우와 개발 방법 이해할 수 있다.<br/>
            • ORM을 활용한 데이터베이스를 조작할 수 있다.<br/>
            • CRUD 기능 구현을 할 수 있다.<br/>
            • 정적 파일과 미디어 파일 처리 방법 이해<br/>
            </td>
        </tr>
        <tr>
            <th rowspan="4">절차</th>
            <td>
                <strong>1. url 및 view 개발</strong><br/>
                • url 패턴과 view 함수 개발 방법<br/>
                • url 매핑과 view 함수 연결 방법<br/>
                • view 함수에서의 요청 처리와 응답 방법<br/>
                • 클래스 기반 뷰의 활용 방법<br/>
                <br/>
                예상 소요 시간 : 20min
            </td>
        </tr>
        <tr>
            <td>
                <strong>2. ORM과 데이터 베이스 조작</strong><br/>
                • ORM 개념과 장점<br/>
                • ORM 활용법<br/>
                <br/>
                예상 소요 시간 : 20min
            </td>
        </tr>
        <tr>
            <td>
                <strong>3. 정적 파일과 미디어 파일</strong><br/>
                • 정적 파일의 활용 방법 이해 <br/>
                • 미디어 파일 업로드 및 처리 방법<br/>
                • 미디어 파일의 url 설정과 접근 방법<br/>
                <br/>
                예상 소요 시간 : 20min
            </td>
        </tr>
        <tr>
            <td>
                <strong>4. Test Case</strong><br/>
                • 테스트 케이스란<br/>
                • 테스트 케이스 작성<br/>
                • (번외) TDD란?<br/>
                <br/>
                예상 소요 시간 : 20min
            </td>
        </tr>
        <tr>
            <th>과제</th>
            <td>2주차에 설계한 DB 모델링 결과 기반 Post, Comment CRUD 구현 및 테스트 케이스 작성</td>
        </tr>
    </tbody>
</table>

### 4주차

<table>
    <tbody>
        <tr>
            <th>트랙</th>
            <td>BE</td>
        </tr>
        <tr>
            <th>날짜</th>
            <td>'23.05.24</td>
        </tr>
        <tr>
            <th>주제</th>
            <td>REST API</td>
        </tr>
        <tr>
            <th>목표</th>
            <td>
            • REST API가 무엇인지 이해할 수 있다.<br/>
            • Django REST Framework를 다룰 수 있다.<br/>
            </td>
        </tr>
        <tr>
            <th rowspan="3">절차</th>
            <td>
                <strong>1. DRF : Django REST Framework</strong><br/>
                • REST API란?<br/>
                &nbsp;&nbsp;&nbsp;
                    - API & RESTful<br/>
                • DRF 설치<br/>
                <br/>
                예상 소요 시간 : 20min
            </td>
        </tr>
        <tr>
            <td>
                <strong>2. Serializer</strong><br/>
                • JSON<br/>
                • Serializer<br/>
                • APIView와 Serializer 예시 코드<br/>
                <br/>
                예상 소요 시간 : 20min
            </td>
        </tr>
        <tr>
            <td>
                <strong>3. Postman </strong><br/>
                • Postman이란<br/>
                • 사용<br/>
                <br/>
                예상 소요 시간 : 20min
            </td>
        </tr>
        <tr>
            <th>과제</th>
            <td>-</td>
        </tr>
    </tbody>
</table>
