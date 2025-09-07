from models import db

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)       # Campo Obrigatório
    description = db.Column(db.String(150))                 # Omitido, nullable=True - Campo Opcional
    status = db.Column(db.String(50), nullable=False, default="Pendente")

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)  # Chave Estrangeira
    user = db.relationship("User", back_populates="tasks")                      # Relacionamento com Tabela User

    def __repr__(self):
        return f"<Task {self.title} - {self.status}>"