from database import SessionLocal
import crud

def run():
    db = SessionLocal()
    print("欢迎使用 To-do 管理 CLI")
    while True:
        print("\n1. 查看列表\n2. 添加事项\n3. 完成事项\n4. 删除事项\n5. 退出")
        choice = input("选择操作：")
        if choice == "1":
            todos = crud.get_todos(db)
            for t in todos:
                status = "✔" if t.completed else "✘"
                print(f"[{status}] {t.id}: {t.title}")
        elif choice == "2":
            title = input("输入待办事项标题：")
            crud.create_todo(db, title=title)
        elif choice == "3":
            todo_id = int(input("输入要完成的事项 ID："))
            crud.mark_complete(db, todo_id)
        elif choice == "4":
            todo_id = int(input("输入要删除的事项 ID："))
            crud.delete_todo(db, todo_id)
        elif choice == "5":
            break
        else:
            print("无效选择")
    db.close()
