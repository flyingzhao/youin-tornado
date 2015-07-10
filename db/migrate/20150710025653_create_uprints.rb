class CreateUprints < ActiveRecord::Migration
  def change
    create_table :uprints do |t|
      t.integer :uorder_id
      t.integer :ufile_id
      t.integer :perpage
      t.integer :copies
      t.string :place
      
      t.timestamps null: false
    end
  end
end
