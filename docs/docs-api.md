# Documentations all enpoint API

this is a documentation of restfull api library management system, base url in local development: <http://127.0.0.1:5000/api>

## Endpoint GET books

- endpoint for get all books data

  | method | endpoint | authentication | authorization |
  | ------ | --------- | -------------- | ------------- |
  | GET | /books | N | N |

- | Request | Params / query |
  | ----- | ------ |
  |req query | title; author; page ; limit |

- example url : <http://127.0.0.1:5000/api/books?title=thealkhemis&author=john&limit=10&page=1>

- response json

```json
{
  "data": [
    {
      "author": "Paulo Coelho",
      "available": true,
      "id": "47996326-9141-432e-8853-8f890475452d",
      "isbn": "9780062315007",
      "published_year": 1988,
      "stock": 1,
      "title": "The Alchemist"
    },
  ],
  "pagination": {
    "limit": 10,
    "page": 3,
    "total": 26,
    "totalPages": 3
  }
}
```

## Endpoint POST new member

- endpoint for create new member

  | method | endpoint | authentication | authorization |
  | ------ | --------- | -------------- | ------------- |
  | POST | /members | Y | Y |

- request body

  ### json

  | key | value |
  | --- | ---- |
  | name | string |
  | email | string |
  | phone | string |
  | address | string |

- response json

```json
{
  "id": "cbdcf96c-4648-44ea-a7ab-74b0bd9a1db2",
  "name": "John Doe",
  "email": "john@gmail.com",
  "phone": "082123458784",
  "address": "address"
}
```

## Borrowing Book

- endpoint for borrow book from database

  | method | endpoint | authentication | authorization |
  | ------ | ------------------------------ | -------------- | ------------- |
  | POST | /borrowings | N | N |

- request body

  ### json

  | key | value |
  | --- | ---- |
  | book_id | uuid |
  | member_id | uuid |

- response json

```json
{
  "data": {
    "book_id": "493655ba-a5c4-49e2-8c0d-5d0af2eef9db",
    "borrow_date": "2025-03-27",
    "id": "09c8e05f-44fc-48d2-acde-318b1a883219",
    "member_id": "e319823e-2051-414d-a8a4-b826656446fe",
    "return_date": null,
    "status": "BORROWED"
  },
  "message": "Book borrowed successfully"
}
```

## Returning Book

- Endpoint returning book

  | method | endpoint | authentication | authorization |
  | ------ | ------------------------------ | -------------- | ------------- |
  | PUT | /borrowings/:id/return | N | N |

- | Request |
  | -----   |
  |request param :id   |

- example url : <http://127.0.0.1:5000/api/borrowings/13edfa79-80be-4094-880a-6ed2422ed09a/return>

- response json

```json
{
  "data": {
    "book_id": "493655ba-a5c4-49e2-8c0d-5d0af2eef9db",
    "borrow_date": "2025-03-27",
    "id": "09c8e05f-44fc-48d2-acde-318b1a883219",
    "member_id": "e319823e-2051-414d-a8a4-b826656446fe",
    "return_date": "2025-03-27",
    "status": "RETURNED"
  },
  "message": "Book returned successfully"
}
```

## Data borrowing books member

- enpoint for get list all data borrowing book member

 | method | endpoint | authentication | authorization |
  | ------ | ------------------------------ | -------------- | ------------- |
  | PUT | /members/:id/borrowings | N | N |

- | Request |
  | -----   |
  |request param :id   |

- example url : <http://127.0.0.1:5000/api/members/13edfa79-80be-4094-880a-6ed2422ed09a/borrwosings>

- response json

```json
{
  "data": [
    {
      "book": {
        "author": "Antoine de Saint-Exupéry",
        "id": "493655ba-a5c4-49e2-8c0d-5d0af2eef9db",
        "isbn": "9780156012195",
        "title": "The Little Prince"
      },
      "borrow_date": "2025-03-26",
      "id": "15186921-fad7-4fca-b081-c1ac96e6f36f",
      "return_date": null,
      "status": "BORROWED"
    },
    {
      "book": {
        "author": "Paulo Coelho",
        "id": "47996326-9141-432e-8853-8f890475452d",
        "isbn": "9780062315007",
        "title": "The Alchemist"
      },
      "borrow_date": "2025-03-26",
      "id": "13edfa79-80be-4094-880a-6ed2422ed09a",
      "return_date": "2025-03-26",
      "status": "RETURNED"
    }
  ],
  "pagination": {
    "limit": 10,
    "page": 1,
    "total": 4,
    "totalPages": 1
  }
}
```
