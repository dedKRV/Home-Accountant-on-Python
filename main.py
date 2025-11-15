import sys
import os
import csv
import uic
import io
import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QHeaderView, QMessageBox, QMainWindow, QDialog, QLabel, QLineEdit, QDialogButtonBox, QFormLayout, QPushButton
from PyQt6.QtCore import QTimer
from PyQt6 import uic
from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtGui import QPixmap, QPainter, QColor, QFont, QPen

template_Main_menu = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>892</width>
    <height>754</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">font: 700 9pt &quot;Bahnschrift Condensed&quot;;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QGroupBox" name="groupBox">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>430</y>
      <width>681</width>
      <height>261</height>
     </rect>
    </property>
    <property name="title">
     <string>Транзакция</string>
    </property>
    <widget class="QPushButton" name="Add_Transaction">
     <property name="geometry">
      <rect>
       <x>440</x>
       <y>210</y>
       <width>231</width>
       <height>41</height>
      </rect>
     </property>
     <property name="text">
      <string>Добавить Транзакцию</string>
     </property>
    </widget>
    <widget class="QDateTimeEdit" name="Data">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>30</y>
       <width>421</width>
       <height>22</height>
      </rect>
     </property>
    </widget>
    <widget class="QRadioButton" name="Income">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>60</y>
       <width>89</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>Доходы</string>
     </property>
     <attribute name="buttonGroup">
      <string notr="true">buttonGroup</string>
     </attribute>
    </widget>
    <widget class="QRadioButton" name="Expenses">
     <property name="geometry">
      <rect>
       <x>230</x>
       <y>52</y>
       <width>89</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>Расходы</string>
     </property>
     <attribute name="buttonGroup">
      <string notr="true">buttonGroup</string>
     </attribute>
    </widget>
    <widget class="QRadioButton" name="Contribution">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>120</y>
       <width>151</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>Пополнение вклада</string>
     </property>
     <attribute name="buttonGroup">
      <string notr="true">buttonGroup</string>
     </attribute>
    </widget>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>240</x>
       <y>90</y>
       <width>49</width>
       <height>21</height>
      </rect>
     </property>
     <property name="text">
      <string>Тип</string>
     </property>
    </widget>
    <widget class="QComboBox" name="Type_income">
     <property name="geometry">
      <rect>
       <x>50</x>
       <y>90</y>
       <width>111</width>
       <height>22</height>
      </rect>
     </property>
     <item>
      <property name="text">
       <string>Перевод</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Пополнение</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Зар. плата</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Прочее</string>
      </property>
     </item>
    </widget>
    <widget class="QTextEdit" name="Comment">
     <property name="geometry">
      <rect>
       <x>440</x>
       <y>50</y>
       <width>231</width>
       <height>151</height>
      </rect>
     </property>
    </widget>
    <widget class="QComboBox" name="Type_Expenses">
     <property name="geometry">
      <rect>
       <x>270</x>
       <y>90</y>
       <width>111</width>
       <height>22</height>
      </rect>
     </property>
     <item>
      <property name="text">
       <string>Переводы</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Магазин</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Ресторан</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Одежда и обувь</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Цифровой товар</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Транспорт</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Медицина</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Развлечения</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Налоги</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Маркетплейс</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Прочее</string>
      </property>
     </item>
    </widget>
    <widget class="QLabel" name="label_2">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>90</y>
       <width>49</width>
       <height>21</height>
      </rect>
     </property>
     <property name="text">
      <string>Тип</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_3">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>230</y>
       <width>49</width>
       <height>21</height>
      </rect>
     </property>
     <property name="text">
      <string>Сумма</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_4">
     <property name="geometry">
      <rect>
       <x>440</x>
       <y>20</y>
       <width>101</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>Комментарий</string>
     </property>
    </widget>
    <widget class="QRadioButton" name="Income_Contribution">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>150</y>
       <width>71</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>Доход</string>
     </property>
     <attribute name="buttonGroup">
      <string notr="true">buttonGroup_3</string>
     </attribute>
    </widget>
    <widget class="QRadioButton" name="Account_Contribution">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>180</y>
       <width>61</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>Счёт</string>
     </property>
     <attribute name="buttonGroup">
      <string notr="true">buttonGroup_3</string>
     </attribute>
    </widget>
    <widget class="QLineEdit" name="Summ">
     <property name="geometry">
      <rect>
       <x>60</x>
       <y>230</y>
       <width>371</width>
       <height>22</height>
      </rect>
     </property>
    </widget>
    <widget class="QRadioButton" name="Account_expenses">
     <property name="geometry">
      <rect>
       <x>240</x>
       <y>130</y>
       <width>89</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>Счёт</string>
     </property>
     <attribute name="buttonGroup">
      <string notr="true">buttonGroup_2</string>
     </attribute>
    </widget>
    <widget class="QRadioButton" name="Contribution_expenses">
     <property name="geometry">
      <rect>
       <x>240</x>
       <y>160</y>
       <width>89</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>Вклад</string>
     </property>
     <attribute name="buttonGroup">
      <string notr="true">buttonGroup_2</string>
     </attribute>
    </widget>
   </widget>
   <widget class="QTabWidget" name="Table">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>881</width>
      <height>411</height>
     </rect>
    </property>
    <property name="currentIndex">
     <number>0</number>
    </property>
    <widget class="QWidget" name="All_table">
     <attribute name="title">
      <string>Вся таблица</string>
     </attribute>
     <widget class="QTableView" name="tableView">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>871</width>
        <height>371</height>
       </rect>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="Income_table">
     <attribute name="title">
      <string>Доходы</string>
     </attribute>
     <widget class="QTableView" name="tableView_2">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>871</width>
        <height>371</height>
       </rect>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="Expenses_table_2">
     <attribute name="title">
      <string>Расходы</string>
     </attribute>
     <widget class="QTableView" name="tableView_3">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>871</width>
        <height>371</height>
       </rect>
      </property>
     </widget>
    </widget>
   </widget>
   <widget class="QLabel" name="error">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>700</y>
      <width>871</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="Save">
    <property name="geometry">
     <rect>
      <x>700</x>
      <y>430</y>
      <width>181</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Сохранить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="Save_where">
    <property name="geometry">
     <rect>
      <x>700</x>
      <y>470</y>
      <width>181</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Сохранить как</string>
    </property>
   </widget>
   <widget class="QPushButton" name="Create_Diogram">
    <property name="geometry">
     <rect>
      <x>700</x>
      <y>510</y>
      <width>181</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Создать диограмму</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="buttonGroup_2"/>
  <buttongroup name="buttonGroup_3"/>
  <buttongroup name="buttonGroup"/>
 </buttongroups>
</ui>
'''

template_Menu = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>571</width>
    <height>361</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">font: 700 15pt &quot;Bahnschrift Condensed&quot;;</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>571</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:28pt;&quot;&gt;Домашняя бухгалтерия&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QPushButton" name="Add_table">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>121</y>
     <width>531</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Создать таблицу (новый месяц)</string>
   </property>
  </widget>
  <widget class="QPushButton" name="Open_table_csv">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>160</y>
     <width>531</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Открыть файл csv,  xlsx (продолжить таблицу)</string>
   </property>
  </widget>
  <widget class="QPushButton" name="Merge_block">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>200</y>
     <width>531</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Объединить в квартал (3 таблицы)</string>
   </property>
  </widget>
  <widget class="QPushButton" name="Combine_year">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>240</y>
     <width>531</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Объединить в годовой отчёт (12 таблиц)</string>
   </property>
  </widget>
  <widget class="QPushButton" name="Open_last_table">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>81</y>
     <width>531</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Открыть последнюю таблицу</string>
   </property>
  </widget>
  <widget class="QLabel" name="error">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>280</y>
     <width>531</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:7pt; font-weight:400; font-style:italic;&quot;&gt;&lt;br/&gt;&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>-2</x>
     <y>50</y>
     <width>571</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;1 месяц - 1 таблица&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>571</width>
     <height>81</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="pixmap">
    <pixmap>Photo.png</pixmap>
   </property>
  </widget>
  <zorder>label_3</zorder>
  <zorder>label</zorder>
  <zorder>Add_table</zorder>
  <zorder>Open_table_csv</zorder>
  <zorder>Merge_block</zorder>
  <zorder>Combine_year</zorder>
  <zorder>Open_last_table</zorder>
  <zorder>error</zorder>
  <zorder>label_2</zorder>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class DatabaseManager:
    def __init__(self, db_path=None):
        if db_path is None:
            if getattr(sys, 'frozen', False):
                exe_dir = os.path.dirname(sys.executable)
                self.db_path = os.path.join(exe_dir, "home_buhgalter.sql")
            else:
                self.db_path = "home_buhgalter.sql"
        else:
            self.db_path = db_path

    def insert_transaction(self, time, transaction_type, amount, comment, category, account_balance, deposit_balance):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO accounting 
                (time, transaction_type, amount, comment, category, account_balance, deposit_balance)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (time, transaction_type, amount, comment, category, account_balance, deposit_balance))

            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Ошибка добавления транзакции в БД: {e}")
            return False

    def sync_csv_to_db(self, csv_data):
        try:
            if len(csv_data) <= 1:
                return

            headers = csv_data[0]
            transactions = csv_data[1:]

            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            for row in transactions:
                if len(row) >= 7:
                    date, transaction_type, amount_str, comment, category, account_balance_str, deposit_balance_str = row[:7]

                    try:
                        amount = float(amount_str)
                        account_balance = float(account_balance_str)
                        deposit_balance = float(deposit_balance_str)

                        cursor.execute('''
                            INSERT INTO accounting 
                            (time, transaction_type, amount, comment, category, account_balance, deposit_balance)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                        ''', (date, transaction_type, amount, comment, category, account_balance, deposit_balance))

                    except ValueError:
                        continue

            conn.commit()
            conn.close()

        except Exception as e:
            print(f"Ошибка синхронизации CSV с БД: {e}")


class InitialBalanceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Начальный баланс")
        self.setFixedSize(400, 150)

        layout = QFormLayout()

        self.main_account_edit = QLineEdit()
        self.main_account_edit.setText("0")
        self.contribution_edit = QLineEdit()
        self.contribution_edit.setText("0")

        layout.addRow("Начальный баланс счета:", self.main_account_edit)
        layout.addRow("Начальный баланс вклада:", self.contribution_edit)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self.validate_and_accept)
        buttons.rejected.connect(self.reject)

        layout.addRow(buttons)
        self.setLayout(layout)

    def validate_and_accept(self):
        try:
            main_balance = float(self.main_account_edit.text())
            contrib_balance = float(self.contribution_edit.text())

            if main_balance < 0 or contrib_balance < 0:
                QMessageBox.warning(self, "Ошибка", "Балансы не могут быть отрицательными")
                return

            self.accept()
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите корректные числа")


class SaveDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Сохранение")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Сохранить изменения?"))

        buttons = QDialogButtonBox()
        self.save_button = buttons.addButton("Сохранить", QDialogButtonBox.ButtonRole.AcceptRole)
        self.save_as_button = buttons.addButton("Сохранить как", QDialogButtonBox.ButtonRole.YesRole)
        self.dont_save_button = buttons.addButton("Не сохранять", QDialogButtonBox.ButtonRole.RejectRole)
        self.cancel_button = buttons.addButton("Отмена", QDialogButtonBox.ButtonRole.RejectRole)

        self.save_button.clicked.connect(self.accept)
        self.save_as_button.clicked.connect(self.save_as)
        self.dont_save_button.clicked.connect(self.reject)
        self.cancel_button.clicked.connect(self.cancel)

        layout.addWidget(buttons)
        self.setLayout(layout)

        self.result_type = "save"

    def save_as(self):
        self.result_type = "save_as"
        self.accept()

    def cancel(self):
        self.result_type = "cancel"
        self.reject()


class ChartDialog(QDialog):
    def __init__(self, expenses_data, parent=None):
        super().__init__(parent)
        self.expenses_data = expenses_data
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Диаграмма расходов")
        self.setFixedSize(800, 600)

        layout = QVBoxLayout()

        self.chart_label = QLabel()
        self.chart_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chart_label.setMinimumSize(700, 500)
        self.chart_label.setStyleSheet("border: 1px solid gray; background-color: white;")

        layout.addWidget(self.chart_label)

        self.close_button = QPushButton("Закрыть")
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

        self.generate_chart()

    def generate_chart(self):
        if not self.expenses_data:
            self.chart_label.setText("Нет данных о расходах для построения диаграммы")
            return

        pixmap = QPixmap(700, 500)
        pixmap.fill(Qt.GlobalColor.white)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        colors = [
            QColor(255, 99, 132),
            QColor(54, 162, 235),
            QColor(255, 205, 86),
            QColor(75, 192, 192),
            QColor(153, 102, 255),
            QColor(255, 159, 64),
            QColor(201, 203, 207),
            QColor(0, 255, 0),
            QColor(255, 0, 255),
            QColor(0, 255, 255)
        ]

        center_x, center_y = 350, 200
        radius = 150
        total_amount = sum(amount for _, amount in self.expenses_data)

        start_angle = 0
        color_index = 0
        legend_items = []

        for expense_type, amount in self.expenses_data:
            percentage = (amount / total_amount) * 100
            angle = (amount / total_amount) * 360 * 16

            painter.setBrush(colors[color_index % len(colors)])
            painter.setPen(QPen(Qt.GlobalColor.black, 2))
            painter.drawPie(center_x - radius, center_y - radius,
                            radius * 2, radius * 2,
                            int(start_angle), int(angle))

            legend_items.append((expense_type, amount, percentage, colors[color_index]))

            start_angle += angle
            color_index += 1

        legend_x = 50
        legend_y = 350
        legend_item_height = 25

        font = QFont()
        font.setPointSize(10)
        painter.setFont(font)

        for i, (expense_type, amount, percentage, color) in enumerate(legend_items):
            painter.setBrush(color)
            painter.drawRect(legend_x, legend_y + i * legend_item_height, 20, 15)

            painter.setPen(Qt.GlobalColor.black)
            legend_text = f"{expense_type}: {amount} ({percentage:.1f}%)"
            painter.drawText(legend_x + 30, legend_y + 15 + i * legend_item_height, legend_text)

        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        painter.setFont(title_font)
        painter.drawText(250, 30, "Диаграмма расходов")

        painter.end()
        self.chart_label.setPixmap(pixmap)


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        template_Menu_2 = io.StringIO(template_Menu)
        uic.loadUi(template_Menu_2, self)
        self.setWindowTitle("Домашний бухгалтер")
        self.setFixedSize(571, 360)

        self.db_manager = DatabaseManager()

        self.Open_last_table.clicked.connect(self.open_last_table)
        self.Add_table.clicked.connect(self.create_table)
        self.Open_table_csv.clicked.connect(self.open_csv_file)
        self.Merge_block.clicked.connect(self.merge_quarter)
        self.Combine_year.clicked.connect(self.merge_year)

        self.last_table_path = None
        self.current_table_window = None

        self.load_last_table_path()

    def get_unique_filename(self, folder_path, base_filename):
        name, ext = os.path.splitext(base_filename)
        counter = 1
        new_filename = base_filename

        while os.path.exists(os.path.join(folder_path, new_filename)):
            new_filename = f"{name}_{counter}{ext}"
            counter += 1

        return new_filename

    def get_config_path(self):
        if getattr(sys, 'frozen', False):
            exe_dir = os.path.dirname(sys.executable)
            return os.path.join(exe_dir, "last_table.txt")
        else:
            return "last_table.txt"

    def save_last_table_path(self, file_path):
        try:
            with open(self.get_config_path(), 'w', encoding='utf-8') as f:
                f.write(file_path)
        except Exception as e:
            print(f"Ошибка сохранения пути: {e}")

    def load_last_table_path(self):
        try:
            if os.path.exists(self.get_config_path()):
                with open(self.get_config_path(), 'r', encoding='utf-8') as f:
                    path = f.read().strip()
                    if os.path.exists(path):
                        self.last_table_path = path
        except Exception as e:
            print(f"Ошибка загрузки пути: {e}")

    def show_error(self, message):
        self.error.setText(message)
        self.error.setStyleSheet("color: red;")
        QTimer.singleShot(5000, lambda: self.error.setText(""))

    def show_success(self, message):
        self.error.setText(message)
        self.error.setStyleSheet("color: green;")
        QTimer.singleShot(5000, lambda: self.error.setText(""))

    def open_last_table(self):
        if self.last_table_path and os.path.exists(self.last_table_path):
            self.open_main_accounting_window(self.last_table_path)
            self.show_success("Последняя таблица открыта!")
        else:
            self.show_error("Последняя таблица не найдена! Создайте новую таблицу.")

    def create_table(self):
        try:
            folder_path = QFileDialog.getExistingDirectory(
                self,
                "Выберите папку для сохранения таблицы",
                ""
            )

            if folder_path:
                dialog = InitialBalanceDialog(self)
                if dialog.exec() == QDialog.DialogCode.Accepted:
                    main_balance = float(dialog.main_account_edit.text())
                    contrib_balance = float(dialog.contribution_edit.text())

                    current_date = datetime.now().strftime("%Y_%m")
                    base_filename = f"бухгалтерия_{current_date}.csv"

                    filename = self.get_unique_filename(folder_path, base_filename)
                    file_path = os.path.join(folder_path, filename)

                    with open(file_path, 'w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            ['Дата', 'Категория', 'Сумма', 'Описание', 'Тип', 'Баланс счета', 'Баланс вклада'])
                        writer.writerow([
                            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            'Начальный баланс',
                            '0',
                            'Начало ведения учета',
                            'Баланс',
                            str(main_balance),
                            str(contrib_balance)
                        ])

                    self.last_table_path = file_path
                    self.save_last_table_path(file_path)
                    self.show_success(f"Таблица создана: {filename}")
                    self.open_main_accounting_window(file_path)

        except Exception as e:
            self.show_error(f"Ошибка при создании таблицы: {str(e)}")

    def open_csv_file(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Выберите CSV файл",
                "",
                "CSV Files (*.csv)"
            )

            if file_path:
                self.last_table_path = file_path
                self.save_last_table_path(file_path)
                self.open_main_accounting_window(file_path)
                self.show_success("CSV файл открыт!")

        except Exception as e:
            self.show_error(f"Ошибка открытия CSV файла: {str(e)}")

    def read_csv_file(self, file_path):
        data = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
            return data
        except Exception as e:
            raise Exception(f"Ошибка чтения файла: {str(e)}")

    def write_csv_file(self, file_path, data):
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for row in data:
                    writer.writerow(row)
        except Exception as e:
            raise Exception(f"Ошибка записи файла: {str(e)}")

    def open_main_accounting_window(self, file_path):
        try:
            data = self.read_csv_file(file_path)
            self.current_table_window = MainAccountingWindow(file_path, data, self.db_manager)
            self.current_table_window.show()
            self.hide()

        except Exception as e:
            self.show_error(str(e))

    def merge_quarter(self):
        try:
            files = []
            for i in range(3):
                file_path, _ = QFileDialog.getOpenFileName(
                    self,
                    f"Выберите {i + 1}-ю таблицу для квартала",
                    "",
                    "CSV Files (*.csv)"
                )
                if file_path:
                    files.append(file_path)
                else:
                    self.show_error("Выбор файлов отменен!")
                    return

            if len(files) != 3:
                self.show_error("Необходимо выбрать ровно 3 файла!")
                return

            all_data = []
            headers = None

            for file in files:
                data = self.read_csv_file(file)
                if not headers:
                    headers = data[0]
                    all_data.append(headers)

                all_data.extend(data[1:])

            if len(all_data) > 1:
                header = all_data[0]
                data_rows = all_data[1:]
                data_rows.sort(key=lambda x: x[0])
                all_data = [header] + data_rows

            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "Сохранить квартальный отчет",
                f"квартальный_отчет_{datetime.now().strftime('%Y_%m')}.csv",
                "CSV Files (*.csv)"
            )

            if save_path:
                self.write_csv_file(save_path, all_data)
                self.last_table_path = save_path
                self.save_last_table_path(save_path)
                self.open_main_accounting_window(save_path)
                self.show_success("Квартальный отчет создан!")

        except Exception as e:
            self.show_error(f"Ошибка при объединении: {str(e)}")

    def merge_year(self):
        try:
            files = []
            for i in range(12):
                file_path, _ = QFileDialog.getOpenFileName(
                    self,
                    f"Выберите {i + 1}-ю таблицу для годового отчета",
                    "",
                    "CSV Files (*.csv)"
                )
                if file_path:
                    files.append(file_path)
                else:
                    self.show_error("Выбор файлов отменен!")
                    return

            if len(files) != 12:
                self.show_error("Необходимо выбрать ровно 12 файлов!")
                return

            all_data = []
            headers = None

            for file in files:
                data = self.read_csv_file(file)
                if not headers:
                    headers = data[0]
                    all_data.append(headers)

                all_data.extend(data[1:])

            if len(all_data) > 1:
                header = all_data[0]
                data_rows = all_data[1:]
                data_rows.sort(key=lambda x: x[0])
                all_data = [header] + data_rows

            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "Сохранить годовой отчет",
                f"годовой_отчет_{datetime.now().strftime('%Y')}.csv",
                "CSV Files (*.csv)"
            )

            if save_path:
                self.write_csv_file(save_path, all_data)
                self.last_table_path = save_path
                self.save_last_table_path(save_path)
                self.open_main_accounting_window(save_path)
                self.show_success("Годовой отчет создан!")

        except Exception as e:
            self.show_error(f"Ошибка при объединении: {str(e)}")


class MainAccountingWindow(QMainWindow):
    def __init__(self, file_path, data, db_manager):
        super().__init__()
        self.file_path = file_path
        self.data = data
        self.db_manager = db_manager
        self.modified = False

        _ = io.StringIO(template_Main_menu)
        uic.loadUi(_, self)

        self.setFixedSize(892, 754)

        self.init_ui()
        self.setup_connections()
        self.load_data_to_tables()

    def init_ui(self):
        self.setWindowTitle(f"Домашняя бухгалтерия - {os.path.basename(self.file_path)}")

        current_datetime = datetime.now()
        self.Data.setDateTime(current_datetime)

        self.setup_tables()

        self.Income.setChecked(True)
        self.on_income_toggled(True)
        self.Account_expenses.setChecked(True)
        self.Income_Contribution.setChecked(True)

        self.Summ.returnPressed.connect(self.Add_Transaction.click)

    def setup_tables(self):
        self.table_all = QTableWidget()
        self.table_income = QTableWidget()
        self.table_expenses = QTableWidget()

        layout_all = QVBoxLayout()
        layout_income = QVBoxLayout()
        layout_expenses = QVBoxLayout()

        layout_all.addWidget(self.table_all)
        layout_income.addWidget(self.table_income)
        layout_expenses.addWidget(self.table_expenses)

        self.All_table.setLayout(layout_all)
        self.Income_table.setLayout(layout_income)
        self.Expenses_table_2.setLayout(layout_expenses)

        if hasattr(self, 'Contribution_table'):
            self.Contribution_table.setParent(None)

        if hasattr(self, 'tableView'):
            self.tableView.setParent(None)
        if hasattr(self, 'tableView_2'):
            self.tableView_2.setParent(None)
        if hasattr(self, 'tableView_3'):
            self.tableView_3.setParent(None)
        if hasattr(self, 'tableView_4'):
            self.tableView_4.setParent(None)

    def setup_connections(self):
        self.Add_Transaction.clicked.connect(self.add_transaction)
        self.Save.clicked.connect(self.save_data)
        self.Save_where.clicked.connect(self.save_as)
        self.Create_Diogram.clicked.connect(self.create_diagram)

        self.Income.toggled.connect(self.on_income_toggled)
        self.Expenses.toggled.connect(self.on_expenses_toggled)
        self.Contribution.toggled.connect(self.on_contribution_toggled)

    def create_diagram(self):
        try:
            expenses_data = self.get_expenses_data()

            if not expenses_data:
                self.show_error("Нет данных о расходах для построения диаграммы!")
                return

            chart_dialog = ChartDialog(expenses_data, self)
            chart_dialog.exec()

        except Exception as e:
            self.show_error(f"Ошибка при создании диаграммы: {str(e)}")

    def get_expenses_data(self):
        expenses_dict = {}

        if len(self.data) <= 1:
            return []

        for row in self.data[1:]:
            if len(row) >= 5:
                category = row[1]
                amount_str = row[2]
                transaction_type = row[4]

                if transaction_type == "Расход":
                    try:
                        amount = float(amount_str)
                        if category in expenses_dict:
                            expenses_dict[category] += amount
                        else:
                            expenses_dict[category] = amount
                    except ValueError:
                        continue

        return list(expenses_dict.items())

    def on_income_toggled(self, checked):
        if checked:
            self.Type_income.setVisible(True)
            self.Type_Expenses.setVisible(False)
            self.Income_Contribution.setVisible(False)
            self.Account_Contribution.setVisible(False)
            self.Account_expenses.setVisible(False)
            self.Contribution_expenses.setVisible(False)

    def on_expenses_toggled(self, checked):
        if checked:
            self.Type_income.setVisible(False)
            self.Type_Expenses.setVisible(True)
            self.Income_Contribution.setVisible(False)
            self.Account_Contribution.setVisible(False)
            self.Account_expenses.setVisible(True)
            self.Contribution_expenses.setVisible(True)

    def on_contribution_toggled(self, checked):
        if checked:
            self.Type_income.setVisible(False)
            self.Type_Expenses.setVisible(False)
            self.Income_Contribution.setVisible(True)
            self.Account_Contribution.setVisible(True)
            self.Account_expenses.setVisible(False)
            self.Contribution_expenses.setVisible(False)

    def show_error(self, message):
        self.error.setText(message)
        self.error.setStyleSheet("color: red;")
        QTimer.singleShot(5000, lambda: self.error.setText(""))

    def show_success(self, message):
        self.error.setText(message)
        self.error.setStyleSheet("color: green;")
        QTimer.singleShot(5000, lambda: self.error.setText(""))

    def get_current_balances(self):
        if len(self.data) <= 1:
            return 0, 0

        last_row = self.data[-1]
        if len(last_row) >= 7:
            try:
                main_balance = float(last_row[5]) if last_row[5] else 0
                contrib_balance = float(last_row[6]) if last_row[6] else 0
                return main_balance, contrib_balance
            except ValueError:
                return 0, 0
        return 0, 0

    def add_transaction(self):
        try:
            date = self.Data.dateTime().toString('yyyy-MM-dd HH:mm:ss')
            amount_text = self.Summ.text().strip()
            comment = self.Comment.toPlainText().strip()

            if not amount_text:
                self.show_error("Введите сумму!")
                return

            try:
                amount = float(amount_text)
                if amount <= 0:
                    self.show_error("Сумма должна быть положительной!")
                    return
            except ValueError:
                self.show_error("Сумма должна быть числом!")
                return

            current_main, current_contribution = self.get_current_balances()

            transaction_type = ""
            category = ""
            new_main_balance = current_main
            new_contrib_balance = current_contribution

            if self.Income.isChecked():
                transaction_type = "Доход"
                category = self.Type_income.currentText()
                new_main_balance = current_main + amount

            elif self.Expenses.isChecked():
                transaction_type = "Расход"
                category = self.Type_Expenses.currentText()

                if self.Account_expenses.isChecked():
                    if current_main < amount:
                        self.show_error("Недостаточно средств на основном счете!")
                        return
                    new_main_balance = current_main - amount
                elif self.Contribution_expenses.isChecked():
                    if current_contribution < amount:
                        self.show_error("Недостаточно средств во вкладе!")
                        return
                    new_contrib_balance = current_contribution - amount

            elif self.Contribution.isChecked():
                if self.Income_Contribution.isChecked():
                    transaction_type = "Вклад_Доход"
                    category = "Доход с вклада"
                    new_contrib_balance = current_contribution + amount

                elif self.Account_Contribution.isChecked():
                    transaction_type = "Вклад_Пополнение"
                    category = "Пополнение вклада"
                    if current_main < amount:
                        self.show_error("Недостаточно средств на основном счете!")
                        return
                    new_main_balance = current_main - amount
                    new_contrib_balance = current_contribution + amount

            new_row = [
                date,
                category,
                str(amount),
                comment,
                transaction_type,
                str(new_main_balance),
                str(new_contrib_balance)
            ]

            if len(self.data) == 0:
                self.data = [['Дата', 'Категория', 'Сумма', 'Описание', 'Тип', 'Баланс счета', 'Баланс вклада'],
                             new_row]
            else:
                self.data.append(new_row)

            self.db_manager.insert_transaction(date, transaction_type, amount, comment, category, new_main_balance,
                                               new_contrib_balance)

            self.load_data_to_tables()

            self.Summ.clear()
            self.Comment.clear()

            self.modified = True
            self.show_success("Транзакция добавлена!")

        except Exception as e:
            self.show_error(f"Ошибка при добавлении транзакции: {str(e)}")

    def load_data_to_tables(self):
        try:
            if len(self.data) <= 1:
                headers = ['Дата', 'Категория', 'Сумма', 'Описание', 'Тип', 'Баланс счета', 'Баланс вклада']
                self.load_table_data(self.table_all, headers, [])
                self.load_table_data(self.table_income, headers, [])
                self.load_table_data(self.table_expenses, headers, [])
                return

            headers = self.data[0]
            all_rows = self.data[1:]

            income_rows = [row for row in all_rows if row[4] == "Доход"]
            expenses_rows = [row for row in all_rows if row[4] == "Расход"]

            self.load_table_data(self.table_all, headers, all_rows)
            self.load_table_data(self.table_income, headers, income_rows)
            self.load_table_data(self.table_expenses, headers, expenses_rows)

        except Exception as e:
            self.show_error(f"Ошибка загрузки данных: {str(e)}")

    def load_table_data(self, table, headers, rows):
        table.setRowCount(len(rows))
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        for i, row in enumerate(rows):
            for j, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                table.setItem(i, j, item)

        header = table.horizontalHeader()
        for i in range(len(headers)):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    def save_data(self):
        try:
            with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for row in self.data:
                    writer.writerow(row)

            self.modified = False
            self.show_success("Данные сохранены!")

        except Exception as e:
            self.show_error(f"Ошибка сохранения: {str(e)}")

    def save_as(self):
        try:
            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "Сохранить как",
                f"бухгалтерия_{datetime.now().strftime('%Y_%m')}.csv",
                "CSV Files (*.csv)"
            )

            if save_path:
                with open(save_path, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    for row in self.data:
                        writer.writerow(row)

                self.db_manager.sync_csv_to_db(self.data)

                self.file_path = save_path
                self.modified = False
                self.setWindowTitle(f"Домашняя бухгалтерия - {os.path.basename(self.file_path)}")
                self.show_success("Данные сохранены в новый файл!")

        except Exception as e:
            self.show_error(f"Ошибка сохранения: {str(e)}")

    def closeEvent(self, event):
        if self.modified:
            dialog = SaveDialog(self)
            result = dialog.exec()

            if dialog.result_type == "cancel":
                event.ignore()
                return
            elif dialog.result_type == "save":
                self.save_data()
                event.accept()
            elif dialog.result_type == "save_as":
                self.save_as()
                event.accept()
            else:
                event.accept()
        else:
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())