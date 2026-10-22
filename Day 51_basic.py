# 🍔 Food Delivery Backend System — System Design

## 📌 About the Project

The **Food Delivery Backend System** is a mini backend simulation developed as part of the Klymb AI System Design challenge.

The project models the basic working of a food delivery platform, where users can browse restaurants, place orders, and track delivery status. It demonstrates how core entities interact and how a backend system can be designed to manage food orders efficiently.

## 🎯 Objectives

* Design core entities and their relationships.
* Create classes for users, restaurants, orders, and delivery tracking.
* Implement a simple order placement flow.
* Simulate order processing and delivery status updates.
* Document important architecture decisions.

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Concepts:** Object-Oriented Programming, System Design, Classes, Relationships
* **Tools:** VS Code, GitHub
* **Challenge Platform:** Klymb AI

## ✨ Features

* 👤 Manage user information.
* 🍽️ Represent restaurants and their menus.
* 🛒 Simulate food order placement.
* 📦 Track order status.
* 🚴 Update delivery progress.
* 🔗 Connect users, restaurants, orders, and deliveries.

## 🏗️ System Architecture

The system consists of four main entities:

| Entity     | Responsibility                                 |
| ---------- | ---------------------------------------------- |
| User       | Places food orders.                            |
| Restaurant | Provides food items and accepts orders.        |
| Order      | Stores order details and manages order status. |
| Delivery   | Tracks the delivery progress of an order.      |

### Order Flow

1. A user selects a restaurant and food items.
2. The user places an order.
3. The system creates an order with an initial status.
4. The restaurant processes the order.
5. The delivery status is updated as the order progresses.
6. The order is marked as delivered when completed.

## 🔄 Example Order Statuses

* `PLACED` — Order has been created.
* `CONFIRMED` — Restaurant has accepted the order.
* `PREPARING` — Food is being prepared.
* `OUT_FOR_DELIVERY` — Order is on its way.
* `DELIVERED` — Order has reached the user.
* `CANCELLED` — Order has been cancelled.

## 🧠 System Design Concepts

| Concept        | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| Entities       | Represent users, restaurants, orders, and deliveries.             |
| Relationships  | Connect users to orders and orders to restaurants and deliveries. |
| Encapsulation  | Keep related data and behavior inside classes.                    |
| Modular Design | Separate responsibilities into manageable components.             |
| Scalability    | Design the system so it can be extended with additional features. |

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd food-delivery-backend
   ```

3. Run the Python program:

   ```bash
   python main.py
   ```

   Replace `main.py` with your actual Python filename if needed.

## 📂 Project Structure

```text
food-delivery-backend/
│
├── main.py
├── README.md
└── architecture.md
```

The `architecture.md` file can contain additional notes about entity relationships, order processing, and design decisions.

## 🌍 Real-World Applications

Similar system design concepts are used in platforms such as:

* Swiggy
* Zomato
* Uber Eats
* Amazon

These platforms use backend systems to coordinate users, businesses, orders, and delivery operations.

## 📚 What I Learned

Through this challenge, I aim to strengthen my understanding of system design, entity relationships, object-oriented programming, and backend workflows. The project provides a foundation for understanding how real-world food delivery platforms organize their core operations.

## 👩‍💻 Author

Created as part of the **Klymb AI System Design Challenge**.

## ⭐ Acknowledgement

Thanks to Klymb AI for providing an opportunity to practice system design through a real-world-inspired project.
