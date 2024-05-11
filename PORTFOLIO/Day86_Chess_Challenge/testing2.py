# ################################### PASTING ##############################################
        if self.clicked_time == 1:
            self.move_to = row, col
            cell_name = self.name_cell(row=row, col=col)

            # ##############################
            if self.previous_piece is None:
                # self.previous_piece can only be None after pasting was successful
                # that is the player tries to double paste
                messagebox.showwarning(title='Empty Hand!', message='No piece to play')
                self.clicked_time = 0

            # ##############################
            elif self.clicked_cell in permissible_starting_cells.keys():
                # that is self-capture is not allowed
                messagebox.showwarning(title='Self Capture!', message="Self capture not permitted!"
                                                                      "\nMove to a cell not occupy by your piece")

                # --------------------------------------
                # return pasting piece to it previous position
                returned_row, returned_column = self.move_from

                returned_cell = self.configure_cell(row=returned_row, col=returned_column,
                                                    image=self.previous_piece_image, piece=self.previous_piece)

                # add returned cell back to the permissible_cells
                permissible_starting_cells[returned_cell] = self.move_from

                # return the Move object at this position
                self.game_logic.update_moves(row=returned_row, col=returned_column, piece=self.previous_piece,
                                             player=self.game_logic.current_player)

                # ----------------------------------------------

                # to avoid double pasting, reset some inherited variables:
                self.previous_piece_image = None
                self.previous_piece = None

                # to penalize this action, toggle to the next player
                self.toggle(_when='penalize')

            # ################################
            else:
                if self.clicked_piece is None:
                    paste_report = (f'{cell_name} now occupied by '
                                    f'{self.previous_piece.color.title()} {self.previous_piece.class_name}')
                else:
                    # ---------------------------------------
                    # remove already occupied piece from its permissible cells
                    if self.clicked_piece.color == 'white':
                        self.occupied_white_pieces.pop(self.clicked_cell)
                    elif self.clicked_piece.color == 'black':
                        self.occupied_black_pieces.pop(self.clicked_cell)

                    # print(f'This cell holds {clicked_piece.color} {clicked_piece.name} before capturing')

                    paste_report = (f'{self.clicked_piece.color.title()} {self.clicked_piece.class_name} '
                                    f'at {cell_name} is captured by {self.previous_piece.color.title()}'
                                    f' {self.previous_piece.class_name}')

                    # ------------------------------------------

                self.animated_display_label.config(text=paste_report)

                # change the current cell at this position to inherit from the previous clicked cell
                new_cell = self.configure_cell(row=row, col=col, image=self.previous_piece_image,
                                               piece=self.previous_piece)

                # add new_cell to the permissible_cells
                permissible_starting_cells[new_cell] = self.move_to

                # update the Move object at this position
                self.game_logic.update_moves(row=row, col=col, piece=self.previous_piece,
                                             player=self.game_logic.current_player)

                # to avoid double pasting, reset some inherited variables:
                self.previous_piece_image = None
                self.previous_piece = None

                # cancel timer after pasting
                self.after_cancel(self.timer_id)

                # toggle after pasting, but only after 3 seconds
                self.toggle_id = self.after(3000, self.toggle, 'pasting')

        # ########################### COPYING ##################################
        elif self.clicked_time == 0:
            self.move_from = row, col

            # ###########################
            if self.clicked_piece is None:
                # you cannot copy a cell with no piece
                messagebox.showerror(title='Invalid Selection!',
                                     message=f'Cell occupies no piece now!\n\n'
                                             f'Please click on a valid {current_player_color.title()} piece')
                self.clicked_time = 0

            # ###########################
            elif self.clicked_cell not in permissible_starting_cells.keys():
                messagebox.showwarning(title='Trespassing!',
                                       message='Ensured to move your own piece')
                self.clicked_time = 0

            # ###########################
            else:
                # set the clicked cell as a previous clicked cell to be used when pasting
                self.previous_piece = self.clicked_piece

                # remove the copied item from permissible_starting_cells
                permissible_starting_cells.pop(self.clicked_cell)

                cell_name = self.name_cell(row=row, col=col)

                copied_report = (f'{self.clicked_piece.color.title()} {self.clicked_piece.class_name} '
                                 f'moves from {cell_name}')
                self.animated_display_label.config(text=f'{copied_report}')

                # update the Move object at that position to loss its piece
                self.game_logic.update_moves(row=row, col=col, piece=None,
                                             player=self.game_logic.current_player)

                # get the piece name and its associated image
                self.previous_piece_image = self.select_image(name=self.clicked_piece.name)

                # reset this cell to the default properties
                self.configure_cell(row=row, col=col, piece=None)

                # increment clicked time to enable pasting
                self.clicked_time += 1