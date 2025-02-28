"use client";

import { cn } from "@/lib/style";
import { useRouter } from "next/navigation";
import { useActionState, useEffect, useState, startTransition } from "react";
import { useToast } from "@/hooks/use-toast";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from "@/components/ui/select";
import {
	Card,
	CardHeader,
	CardTitle,
	CardContent,
} from "@/components/ui/card";
import { createAction } from "@/server-actions/chatbot-index/create";
import { X, SendHorizonal, FileText } from "lucide-react"

type Props = {
	chatbotId: string
	className?: string;
};

const resources = [
	{ value: 'openai', label: 'OpenAI', isDisabled: false },
	{ value: 'google', label: 'Google', isDisabled: true },
	{ value: 'anthropic', label: 'Anthropic', isDisabled: true },
]

export const CreateChatbotIndexForm = ({ chatbotId, className }: Props) => {
	const router = useRouter();
	const { toast } = useToast();
	const [docs, setDocs] = useState<File[]>([]);
	

	const [state, formAction, isPending] = useActionState(createAction, {
		inputs: {
			chatbotId: chatbotId,
			resource: "openai",
			title: "",
			content: "",
			docs: []
		},
	});

	useEffect(() => {
		if (state.success) {
			toast({
				title: "Success",
				description: "Create Chatbot Successfully",
			});
			router.push("/chatbot");
		} else if (state.success === false) {
			toast({
				variant: "destructive",
				title: "Error",
				description: "Error while Creating Chatbot",
			});
		}
	}, [state]);

	const handleDocsChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		const selected = e.target.files;
		if (!selected) return; // null チェック
		setDocs((prev) => [...prev, ...Array.from(selected)]);
	};

	const handleRemoveDoc = (index: number) => {
		setDocs((prev) => prev.filter((_, i) => i !== index));
	};

	const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		const formData = new FormData(e.currentTarget);

		// 書類ファイルを追加
		Array.from(docs).forEach((doc) => formData.append("inputs.docs[]", doc));

		startTransition(() => {
			formAction(formData);
		})
	};

	return (
		<form
			onSubmit={handleSubmit}
			className={cn(
				`w-full flex flex-col justify-center items-center`,
				className,
			)}
		>
			<Card className={`w-full`}>
				<CardHeader className={'flex flex-row items-center justify-between'}>
					<CardTitle>Chat Index</CardTitle>
					<div className={"flex gap-3"}>
						<Label className={'flex items-center justify-between gap-1.5'}>
							LLM
							<Select
								key={state.inputs?.resource}
								name={"inputs.resource"}
								defaultValue={state.inputs?.resource}
							>
								<SelectTrigger className="w-[120px]">
									<SelectValue />
								</SelectTrigger>
								<SelectContent>
									{resources.map((resource, i) => <SelectItem key={i} value={resource.value} disabled={resource.isDisabled}>{resource.label}</SelectItem>)}
								</SelectContent>
							</Select>
						</Label>
					</div>
				</CardHeader>
				<CardContent className="flex flex-col gap-3">
					<Input
						type={"hidden"}
						key={state.inputs?.chatbotId}
						name={"inputs.chatbotId"}
						defaultValue={state.inputs?.chatbotId}
					/>
					<Label className={'flex flex-col gap-1.5'}>
						Title
						<Input
							type={"text"}
							name={"inputs.title"}
							defaultValue={state.inputs?.title}
							className={state.validationErrors?.title && "bg-red-200"}
						/>
						{state.validationErrors?.title && (
							<small>{state.validationErrors?.title}</small>
						)}
					</Label>
					<Label className={'flex flex-col gap-1.5'}>
						Content
						<Textarea
							className={"resize-none h-96"}
							key={state.inputs?.content}
							name={"inputs.content"}
							defaultValue={state.inputs?.content}
							placeholder={""}
						/>
						{state.validationErrors?.content && (
							<small>{state.validationErrors?.content}</small>
						)}
					</Label>

					{/* 書類プレビューエリア */}
					{docs.length > 0 && (
						<div className="flex flex-wrap gap-2">
						{docs.map((doc, index) => {
							return (
								<div key={index} className="relative flex items-center gap-2 p-2 bg-gray-100 rounded-md">
									<span className="text-sm text-gray-600">{doc.name}</span>
									<Button
										type="button"
										variant={"ghost"}
										size={"icon"}
										onClick={() => handleRemoveDoc(index)}
										className="w-5 h-5 absolute -top-2 -left-2 rounded-full bg-slate-700/70"
									>
										<X size={16} />
									</Button>
								</div>
							);
						})}
						</div>
					)}

					<div className="flex justify-between items-center w-full mt-2 px-2">
						{/* 添付ボタン（左下） */}
						<div className={"flex items-center gap-1.5"}>
							{/* Docs */}
							<div>
								<Input
									type="file"
									accept=".pdf,.md"
									multiple
									onChange={handleDocsChange}
									id="docs-upload"
									className="hidden"
								/>
								<Button
									type="button"
									variant="outline"
									size="icon"
									onClick={() => document.getElementById("docs-upload")?.click()}
								>
									<FileText size={24} />
								</Button>
							</div>
						</div>

						{/* 送信ボタン（右下） */}
						<Button type="submit" size="icon" disabled={isPending}>
							<SendHorizonal size={24} />
						</Button>
					</div>
				</CardContent>
			</Card>
		</form>
	);
};
